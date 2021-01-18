from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config')

    from reportapp import home
    from reportapp import commercial
    from reportapp import acctmgt
    from reportapp import vertical
    from reportapp.models import db

    return app
