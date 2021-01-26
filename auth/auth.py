from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify

from auth.forms import SignIn, SignUp, ValidationError

from reportapp.models import Verticaluser

import bcrypt

authpage = Blueprint('authpage', __name__, static_folder="static",
                     template_folder="templates")


@authpage.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUp()
    email = form.email.data
    if email:
        verticaluser = Verticaluser.query.filter_by(
            email=email).one()
        if not verticaluser:
            raise ValidationError('Email Not Authorized, Contact Admin')
        else:
            form.vertical.choices = [
                (str(verticaluser.vertical), str(verticaluser.vertical))]
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        name = email.split('@')[0].title()
        vertical = form.vertical.data
        password = form.password.data
        flash(f'Account created for {name}!', 'success')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return f'<h1> Email: {email}, Vertical: {vertical}, password: {password}, hashed: {hashed}</h1>'
        redirect(url_for('/login'))
    return render_template('register.html', title='Sign Up', form=form)


@ authpage.route('/login')
def signin():
    form = SignIn()
    return render_template('login.html', title='Sign In', form=form)


@ authpage.route('/users', methods=['GET'])
def get_all_users():
    return ''


@ authpage.route('/users/<email>', methods=['GET'])
def get_one_user(email):
    user = Verticaluser.query.filter_by(email=email).one()
    userObj = {}
    userObj['id'] = user.id
    userObj['email'] = user.email
    userObj['vertical'] = user.vertical
    return jsonify(userObj)


@ authpage.route('/users/create', methods=['POST'])
def create_user():

    return ''


@ authpage.route('/users/<user_id>', methods=['DELETE'])
def delete_user():
    return ''


@ authpage.route('/users/<user_id>', methods=['PUT'])
def promote_user():
    return ''
