import os
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from reportapp.models import *
from flask_sqlalchemy import SQLAlchemy
from reportapp.home import homepage
from flask_migrate import Migrate
from auth.auth import authpage


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(homepage, url_prefix="")
    app.register_blueprint(authpage, url_prefix="")
    return app


app = create_app()
migrate = Migrate(app, db)
