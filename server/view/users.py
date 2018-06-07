from abc import ABC, abstractmethod
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from werkzeug.local import LocalProxy
from server.storage import models


class User(ABC):
    """Represent abstraction of user."""

    @abstractmethod
    def login(self, user: models.User, form: FlaskForm) -> bool:
        pass

    @abstractmethod
    def logout(self) -> bool:
        pass

    @abstractmethod
    def authenticated(self) -> bool:
        pass

    @abstractmethod
    def image_file(self) -> str:
        pass

    @abstractmethod
    def username(self) -> str:
        pass

    @abstractmethod
    def email(self) -> str:
        pass


class CurrentUser(User):
    """Represent simple user of a blog."""

    def __init__(self) -> None:
        self._user: LocalProxy = current_user

    @property
    def get_user(self) -> LocalProxy:
        return self._user

    @property
    def image_file(self) -> str:
        return self._user.image_file

    @property
    def username(self) -> str:
        return self._user.username

    @property
    def email(self) -> str:
        return self._user.email

    def login(self, user: models.User, form: FlaskForm) -> bool:
        return login_user(user, remember=form.remember.data)

    def logout(self) -> bool:
        return logout_user()

    def authenticated(self) -> bool:
        return self._user.is_authenticated
