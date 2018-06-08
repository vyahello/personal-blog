from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Field, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from server.storage.models import User
from server.view.validations import Validation, ValidationField
from server.view.pages import InformPage
from server.types import Inform
from server.view.users import CurrentUser
from server.view import users


class GenericForm(object):
    """Represent generic form."""

    email: Field = StringField('Email', [DataRequired(), Email()])
    password: Field = PasswordField('Password', [DataRequired()])


class RegistrationForm(FlaskForm, GenericForm):
    """Represent registration page."""

    username: Field = StringField('Username', [DataRequired(), Length(min=2, max=20)])
    confirm_password: Field = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit: Field = SubmitField('Sign Up')
    validation: Validation = ValidationField(User.query)

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
    validation: Validation = ValidationField(User.query)
    user: users.User = CurrentUser()
    inform: Inform = InformPage('Your account has been updated!', 'success', 'account')

    def success(self) -> str:
        return self.inform.perform()

    def validate_username(self, username: User) -> None:
        if username.data != self.user.username:
            self.validation.validate_username(username)

    def validate_email(self, email: User) -> None:
        if email.data != self.user.email:
            self.validation.validate_email(email)


class PostForm(FlaskForm):
    """Represent post form page."""

    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
    inform: Inform = InformPage('Your post has been updated!', 'success', 'home')

    def success(self) -> str:
        return self.inform.perform()
