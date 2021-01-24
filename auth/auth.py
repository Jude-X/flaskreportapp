from flask import Blueprint, render_template, url_for, flash, redirect
from auth.forms import SignIn, SignUp

authpage = Blueprint('authpage', __name__, static_folder="static",
                     template_folder="templates")


@authpage.route('/register')
def signup():
    form = SignUp()
    return render_template('register.html', title='Sign Up', form=form)


@authpage.route('/login')
def signin():
    form = SignIn()
    return render_template('login.html', title='Sign In', form=form)
