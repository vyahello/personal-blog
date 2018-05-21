from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from server.storage.models import User


class GenericForm(object):
    """Represent generic form."""

    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegistrationForm(FlaskForm, GenericForm):
    """Represent registration page."""

    username = StringField('Username', [DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is takes. Please choose different one')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('That email is takes. Please choose different one')


class LoginForm(FlaskForm, GenericForm):
    """Represent registration page."""

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
