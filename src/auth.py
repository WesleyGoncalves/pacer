from . import db
from .enums import Roles
from .models import Team, Member
from flask import Blueprint, request, redirect, url_for, render_template, flash
from sqlalchemy.orm import contains_eager
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_attempt():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False
    next = request.args.get("next")

    # Get member
    member = (
        db.session.query(Member)
        .filter(Member.email == email)
        .order_by(Member.created_at.desc())
        .first()
    )

    # check if the member actually exists and password is correct
    if (
        not member
        or password is None
        or not check_password_hash(member.password, password)
    ):
        flash("E-mail ou senha incorretos.")
        return redirect(url_for("auth.login", next=next))

    login_user(member, remember=remember)

    if next:
        return redirect(next)
    return redirect(url_for("main.index"))


@auth.route("/register")
def register():
    team = None
    if current_user.is_authenticated:
        team = (
            db.session.query(Team)
            .join(Team.members)
            .filter(Team.id == current_user.team_id)
            .first()
        )

    return render_template(
        "register.html",
        team=team,
        Roles=Roles,
        MAX_MEMBERS=Team.MAX_MEMBERS,
    )


@auth.route("/register", methods=["POST"])
def register_store():
    try:

        team = Team(name=request.form.get("team_name"))

        members = []
        # PO
        po_name = request.form.get("product_owner_name")
        if po_name:
            pass_po = generate_password_hash(
                request.form["product_owner_password"], "scrypt"
            )
            members.append(
                Member(
                    name=po_name,
                    email=request.form["product_owner_email"],
                    password=pass_po,
                    role=Roles.PO.name,
                    team=team,
                )
            )
        # Master
        master_name = request.form.get("scrum_master_name")
        if master_name:
            pass_master = generate_password_hash(
                request.form["scrum_master_password"], "scrypt"
            )
            members.append(
                Member(
                    name=master_name,
                    email=request.form["scrum_master_email"],
                    password=pass_master,
                    role=Roles.SM.name,
                    team=team,
                )
            )
        # Scrum Team
        for i in range(1, Team.MAX_MEMBERS - 1):
            prefix = f"team_member_{i}"
            pass_member = None
            member_name = request.form.get(f"{prefix}_name")
            if member_name:
                pass_member = generate_password_hash(
                    request.form[f"{prefix}_password"], "scrypt"
                )
                members.append(
                    Member(
                        name=member_name,
                        email=request.form.get(f"{prefix}_email"),
                        password=pass_member,
                        role=Roles.ST.name,
                        team=team,
                    )
                )

        db.session.add(team)
        for mem in members:
            db.session.add(mem)

        db.session.commit()
    except:
        return "500 Internal Error"

    return redirect(url_for("main.projects"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
