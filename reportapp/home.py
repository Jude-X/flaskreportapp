from flask import Blueprint, render_template, url_for, flash, redirect
from auth.forms import SignIn, SignUp

homepage = Blueprint('homepage', __name__, static_folder="static",
                     template_folder="templates")


@homepage.route('/')
@homepage.route('/home')
def home():
    return render_template('home.html')
