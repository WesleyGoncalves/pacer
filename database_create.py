# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()


# App
from src import create_app

app = create_app()


# Create database
from sqlalchemy_utils import create_database, database_exists

mysql_uri = app.config["SQLALCHEMY_DATABASE_URI"]

if not database_exists(mysql_uri):
    create_database(mysql_uri)


# Create tables
from src import db, models

with app.app_context():
    db.create_all()
