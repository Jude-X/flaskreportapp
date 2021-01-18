from reportapp import app
from flask import render_template, url_for, flash, redirect
from reportapp.models import
from reportapp.forms import SignIn, SignUp


@app.route('/')
@app.route('/home')
def home():
    return return_template('home.html')


@app.route('/signup')
def register():
    form = SignUp()
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login')
def register():
    form = SignIn()
    return render_template('login.html', title='Sign In', form=form)
