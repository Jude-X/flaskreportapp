import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('HEROKU_POSTGRESQL_GOLD_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False
