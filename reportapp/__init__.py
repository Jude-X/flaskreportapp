import os
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_sqlalchemy import SQLAlchemy
from main.home import homepage


def create_app(homepage, test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(homepage, url_prefix="")

    return app


app = create_app(homepage)
