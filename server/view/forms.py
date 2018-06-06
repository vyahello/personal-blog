from abc import ABC, abstractmethod
import secrets
import os
from typing import Tuple
from PIL import Image
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Field
from wtforms.validators import DataRequired, Length, Email, EqualTo
from server import WebServer
from server.storage.models import User
from server.storage.queries import Query, UserQuery
from server.types import Update
from server.view.flashes import PageFlash, Flash
from server.view.redirects import PageRedirect, Redirect
from server.view.urls import PageUrlFor
from server.view.users import CurrentUser
from server.view import users


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


class UpdateAccountForm(FlaskForm, GenericForm):
    """Represent registration page."""

    username: Field = StringField('Username', [DataRequired(), Length(min=2, max=20)])
    submit: Field = SubmitField('Update')
    picture = FileField('Updated Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    validation: Validation = ValidationForm(User.query)
    user: users.User = CurrentUser()
    flash: Flash = PageFlash('Your account has been updated!', 'success')
    redirect: Redirect = PageRedirect(PageUrlFor('account'))

    def success(self) -> str:
        self.flash.display()
        return self.redirect.link()

    def validate_username(self, username: User) -> None:
        if username.data != self.user.username:
            self.validation.validate_username(username)

    def validate_email(self, email: User) -> None:
        if email.data != self.user.email:
            self.validation.validate_email(email)


class UpdateImage(Update):
    """Update user image."""

    def __init__(self, form_picture: FlaskForm, blog: WebServer) -> None:
        self._form = form_picture
        self._blog = blog
        self._image = Image
        self._res: Tuple[int, int] = (125, 125)
        self._pic_path: str = 'static/accounts'

    def save(self) -> str:
        data = self._form.picture.data
        random_hex: str = secrets.token_hex(8)
        _, f_ext = os.path.splitext(data.filename)
        picture_fn: str = random_hex + f_ext
        picture_path: str = os.path.join(self._blog.root_path, self._pic_path, picture_fn)
        output_size: Tuple[int, int] = self._res
        image: Image = self._image.open(data)
        image.thumbnail(output_size)
        image.save(picture_path)
        return picture_fn
