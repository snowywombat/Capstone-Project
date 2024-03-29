from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def first_name_validator(form, field):
    first_name = field.data
    if len(field.data) < 2 or len(field.data) > 20 :
        raise ValidationError('First name must be between 1 and 20 characters.')

def last_name_validator(form, field):
    last_name = field.data
    if len(field.data) < 2 or len(field.data) > 20 :
        raise ValidationError('Last name must be between 1 and 20 characters.')

def username_validator(form, field):
    username = field.data
    if len(field.data) < 2 or len(field.data) > 20 :
        raise ValidationError( 'Username must be between 1 and 20 characters.')

def password_validator(form, field):
    password = field.data
    if len(field.data) < 5 or len(field.data) > 20 :
        raise ValidationError( 'Password must be between 6 and 20 characters.')


class SignUpForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired(), first_name_validator])
    last_name = StringField('last_name', validators=[DataRequired(), last_name_validator])
    username = StringField(
        'username', validators=[DataRequired(), username_exists, username_validator])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired(), password_validator])
