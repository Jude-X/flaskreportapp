from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError


def domain_validator(self, field):
    domain = field.data.split('a')[1]
    if domain != 'flutterwavego.com':
        raise ValidationError('Invalid Email Address')


pswdregexp = '''
    (                   # Start of group
        (?=.*\d)  # must contain at least one digit
        (?=.*[A-Z])  # must contain at least one uppercase character
        (?=.*[a-z])  # must contain at least one lowercase character
        (?=.*\W)  # must contain at least one special symbol
        \w
        .  # match anything with previous condition checking
        {6, 18}  # length is  characters
        \w
    )                   # End of group
    '''

pswdmsg = '''
        Password must contain at least:

        1 uppercase letter
        1 lowercase letter
        1 number
        1 special character
        8-20 characters
            '''


def email_validator(c):
    pass


class SignUp(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(), domain_validator, email_validator])

    vertical = SelectField('Vertical', choices=[])  # signupteamname)
    password = PasswordField('Password', validators=[
                             DataRequired(), Regexp(pswdregexp, message=pswdmsg)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class SignIn(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
