from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class GenericForm(object):
    """Represent generic form."""

    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegistrationForm(FlaskForm, GenericForm):
    """Represent registration page."""

    username = StringField('Username', [DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm, GenericForm):
    """Represent registration page."""

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
