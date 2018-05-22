from abc import ABC, abstractmethod
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Field
from wtforms.validators import DataRequired, Length, Email, EqualTo
from server.storage.models import User
from server.storage.queries import Query, UserQuery


class Validation(ABC):
    """Represent abstraction for some validation."""

    @abstractmethod
    def validate_username(self, username: User) -> None:
        pass

    @abstractmethod
    def validate_email(self, email: User) -> None:
        pass


class ValidationForm(Validation):
    """Represent validation form object."""

    def __init__(self, user: User) -> None:
        self._query: Query = UserQuery(user)

    def validate_username(self, username: User) -> None:
        self._query.first(username=username.data)

    def validate_email(self, email: User) -> None:
        self._query.first(email=email.data)


class GenericForm(object):
    """Represent generic form."""

    email: Field = StringField('Email', [DataRequired(), Email()])
    password: Field = PasswordField('Password', [DataRequired()])


class RegistrationForm(FlaskForm, GenericForm):
    """Represent registration page."""

    username: Field = StringField('Username', [DataRequired(), Length(min=2, max=20)])
    confirm_password: Field = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit: Field = SubmitField('Sign Up')
    validation: Validation = ValidationForm(User.query)

    def validate_username(self, username: User) -> None:
        self.validation.validate_username(username)

    def validate_email(self, email: User) -> None:
        self.validation.validate_email(email)


class LoginForm(FlaskForm, GenericForm):
    """Represent login page."""

    remember: Field = BooleanField('Remember Me')
    submit: Field = SubmitField('Login')
