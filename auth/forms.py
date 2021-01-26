from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from reportapp.models import Verticaluser


emailregexp = "^[a-z]+@flutterwavego\.com$"

emailmsg = "Please Enter A Valid Email Address"

pswdregexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[A-Za-z\d\W]{8,}$"

pswdmsg = '''
        Password must contain at least:

        1 uppercase letter
        1 lowercase letter
        1 number
        1 special character
        8 or more characters
            '''


class SignUp(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(message='Please Fill This Field'), Email(), Regexp(emailregexp, message=emailmsg)])
    vertical = SelectField('Vertical', coerce=str, choices=[], validators=[
        DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), Regexp(pswdregexp, message=pswdmsg)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Sign Up')


class SignIn(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
