from .models import Base, Member
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db: SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()  # load all the env vars prefixed with 'FLASK_'
    app.config.from_prefixed_env("APP")  # load all the env vars prefixed with 'APP_'
    # app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
    # app.config["SESSION_TYPE"] = os.environ.get("FLASK_SESSION_TYPE")

    create_sql_alchemist(app)

    create_authenticator(app)

    register_blueprints(app)

    register_jinja_filters(app)

    return app


def register_blueprints(app: Flask) -> None:
    """Register blueprints (routes)"""

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)


def register_jinja_filters(app):

    from .enums import to_string as enum_to_string_filter

    app.add_template_filter(enum_to_string_filter)


def create_sql_alchemist(app: Flask) -> SQLAlchemy:
    """Initialize a SQLAlchemy instance"""

    global db

    db = SQLAlchemy(model_class=Base)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql://{app.config['DB_USER']}:{app.config['DB_PASS']}"
        f"@{app.config['DB_HOST']}/{app.config['DB_NAME']}"
    )
    db.init_app(app)

    return db


def create_authenticator(app: Flask) -> LoginManager:
    """Initialize a Flask Login instance"""
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Faça login para acessar esse conteúdo."
    login_manager.login_message_category = "danger"
    login_manager.init_app(app)

    # A user loader tells Flask-Login how to find a specific user from the ID that is stored in their session cookie
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(Member).filter(Member.id == user_id).first()
