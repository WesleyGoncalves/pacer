from . import db
from .enums import Principles, Roles
from .models import Team, Member, Project, Score
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import and_
from werkzeug.security import generate_password_hash


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/what-is-pacer")
def what_is_pacer():
    return render_template("what-is-pacer.html")


@main.route("/how-to-evaluate-using-pacer")
def how_to_evaluate_using_pacer():
    return render_template("how-to-evaluate-using-pacer.html")


# PROJECTS --
@main.route("/projects", defaults={"id": None})
@main.route("/projects/<int:id>")
@login_required
def projects(id: int | None):
    projects = (
        db.session.query(Project)
        .filter(Project.team_id == current_user.team_id)
        .order_by(Project.created_at.desc())
        .all()
    )

    proj = None
    if id:
        # get the project with ID from URL
        proj = list(filter(lambda proj: proj.id == id, projects))[0]

    return render_template("projects.html", projects=projects, proj=proj)


@main.route("/projects", methods=["POST"])
@login_required
def projects_store():
    try:
        # get logged user's team
        user_id = current_user.id
        team = db.session.execute(
            db.select(Team).where(Team.members.any(Member.id == user_id))
        )
        team = team.first()[0]

        # project
        project = Project(
            name=request.form["project_name"],
            n_sprints=request.form["n_sprints"],
            team=team,
        )

        db.session.add(project)
        db.session.commit()
    except:
        return "500 Internal Error"

    return redirect(url_for("main.projects"))


@main.route("/projects/update/<int:id>", methods=["POST"])
@login_required
def projects_update(id: int):
    try:
        project = db.get_or_404(Project, id)

        project.name = (request.form["project_name"],)
        project.n_sprints = (request.form["n_sprints"],)

        db.session.commit()
    except:
        return "500 Internal Error"

    return redirect(url_for("main.projects"))


@main.route("/projects/delete/<int:id>", methods=["GET"])
@login_required
def projects_delete(id: int):
    project = (
        db.session.query(Project)
        .filter(
            and_(
                Project.team_id == current_user.team_id,
                Project.id == id,
            )
        )
        .first()
    )

    db.session.delete(project)
    db.session.commit()

    return redirect(url_for("main.projects"))


# TEAM AND MEMBERS --
@main.route("/team")
@login_required
def team():
    team = (
        db.session.query(Team)
        .filter(Team.id == current_user.team_id)
        .order_by(Team.created_at.desc())
        .first()
    )

    return render_template("team.html", team=team)


@main.route("/team/update/<int:id>", methods=["POST"])
@login_required
def team_update(id: int):
    try:
        team = (
            db.session.query(Team)
            .filter(
                and_(Team.id == current_user.team_id, Team.id == id)
            )  # id is redundant
            .order_by(Team.created_at.desc())
            .first()
        )

        if not team:
            flash("404 Equipe não encontrada.")
            return redirect(url_for("main.team"))

        team.name = request.form["team_name"]

        db.session.add(team)
        db.session.commit()
    except:
        flash("500 Erro interno. Se o problema persistir, contate o administrador.")

    return redirect(url_for("main.team"))


@main.route("/members", methods=["POST"])
@login_required
def members_store():
    try:
        team = (
            db.session.query(Team)
            .filter(Team.id == current_user.team_id)
            .order_by(Team.created_at.desc())
            .first()
        )

        if Team.MAX_MEMBERS == len(team.members):
            flash("O tamanho máximo da equipe foi atingido.")
            return redirect(url_for("main.team"))

        password = generate_password_hash(request.form.get("member_password"), "scrypt")
        role = Roles[request.form["role"]]
        member = Member(
            name=request.form["member_name"],
            email=request.form["member_email"],
            password=password,
            role=role,
            team=team,
        )

        # should replace current PO or SM
        if member.role in (Roles.SM, Roles.PO):
            member2 = (
                db.session.query(Member)
                .filter(
                    and_(
                        Member.team_id == member.team_id,
                        Member.role == member.role,
                    )
                )
                .first()
            )
            member2.role = Roles.ST
            db.session.add(member2)

        db.session.add(member)
        db.session.commit()
    except:
        flash("500 Erro interno. Se o problema persistir, contate o administrador.")

    return redirect(url_for("main.team"))


@main.route("/members/update/<int:id>", methods=["POST"])
@login_required
def members_update(id: int):
    """update member on the database whose ID is {id}"""
    try:

        member = (
            db.session.query(Member)
            .filter(
                and_(
                    Member.team_id == current_user.team_id,
                    Member.id == id,
                )
            )
            .first()
        )

        if not member:
            flash("404 Membro não encontrado.")
            return redirect(url_for("main.team"))

        # check if member was PO or SM and is becoming ST
        if (
            member.role in (Roles.SM, Roles.PO)
            and request.form["role"] == Roles.ST.name
        ):
            flash(
                f"Não foi possível alterar o registro. Antes de tornar o {member.role.value.title()} um {Roles.ST.value}, atribua outro membro ao papel de {member.role.value.title()}."
            )
            return redirect(url_for("main.team"))

        # should replace current PO or SM
        role = Roles[request.form["role"]]
        if role in (Roles.SM, Roles.PO):
            member2 = (
                db.session.query(Member)
                .filter(
                    and_(
                        Member.team_id == member.team_id,
                        Member.role == role,
                    )
                )
                .first()
            )
            member2.role = Roles.ST
            db.session.add(member2)

        member.name = request.form["member_name"]
        member.email = request.form["member_email"]
        member.role = role

        if request.form["member_password"]:
            password = generate_password_hash(request.form["member_password"], "scrypt")
            member.password = password

        db.session.add(member)
        db.session.commit()
    except:
        flash("500 Erro interno. Se o problema persistir, contate o administrador.")

    return redirect(url_for("main.team"))


@main.route("/members/delete/<int:id>")
@login_required
def members_delete(id: int):
    member = (
        db.session.query(Member)
        .filter(
            and_(
                Member.team_id == current_user.team_id,
                Member.id == id,
            )
        )
        .first()
    )

    db.session.delete(member)
    db.session.commit()

    return redirect(url_for("main.team"))


# SCORES --
@main.route("/evaluate")
@login_required
def evaluate():
    # read projects
    projects = (
        db.session.query(Project)
        .filter(Project.team_id == current_user.team_id)
        .order_by(Project.created_at.desc())
        .all()
    )

    # scores list
    scores = (
        db.session.query(Score)
        .order_by(
            Score.project_id.desc(),
            Score.n_sprint.desc(),
            Score.member_id.asc(),
        )
        .all()
    )

    return render_template("evaluate.html", projects=projects, scores=scores)


@main.route("/scores")
@login_required
def scores():
    # scores list
    scores = (
        db.session.query(Score)
        .order_by(
            Score.project_id.desc(),
            Score.n_sprint.desc(),
            Score.member_id.asc(),
        )
        .all()
    )

    return render_template("scores.html", scores=scores)


@main.route("/score", methods=["POST"])
@login_required
def scores_store():
    try:
        # get logged member/user
        member = current_user

        # get project - make sure it exists
        project = (
            db.session.query(Project)
            .filter(
                and_(
                    Project.team_id == member.team.id,
                    Project.id == request.form.get("project_id"),
                )
            )
            .first()
        )

        # get n_sprint
        n_sprint = request.form.get("n_sprint")

        # Scores
        score = Score(
            n_sprint=n_sprint,
            score_proatividade=request.form.get("proatividade"),
            score_autonomia=request.form.get("autonomia"),
            score_colaboracao=request.form.get("colaboracao"),
            score_entrega=request.form.get("entrega"),
            member=member,
            project=project,
        )

        db.session.add(score)
        db.session.commit()
    except:
        return "500 Internal Error"

    return redirect(url_for("main.scores"))


@main.route("/scores/delete/<int:id>", methods=["GET"])
def scores_delete(id: int):
    score = db.session.query(Score).filter(Score.id == id).first()

    if score.member.team_id == current_user.team_id:
        db.session.delete(score)
        db.session.commit()

    return redirect(url_for("main.scores"))
