from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config')

    from models import db

    return app
