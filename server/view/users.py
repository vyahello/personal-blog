from abc import ABC, abstractmethod
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
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
    def image_file(self):
        pass


class OrdinaryUser(User):
    """Represent simple user of a blog."""

    def login(self, user: models.User, form: FlaskForm) -> bool:
        return login_user(user, remember=form.remember.data)

    def logout(self) -> bool:
        return logout_user()

    def authenticated(self) -> bool:
        return current_user.is_authenticated

    def image_file(self):
        return current_user.image_file
