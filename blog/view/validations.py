from abc import ABC, abstractmethod
from blog.storage.models import User
from blog.storage.queries import Query, UserQuery


class Validation(ABC):
    """Represent abstraction for some validation."""

    @abstractmethod
    def validate_username(self, username: User) -> None:
        pass

    @abstractmethod
    def validate_email(self, email: User) -> None:
        pass


class ValidationField(Validation):
    """Represent validation form object."""

    def __init__(self, user: User) -> None:
        self._query: Query = UserQuery(user)

    def validate_username(self, username: User) -> None:
        self._query.first(username=username.data)

    def validate_email(self, email: User) -> None:
        self._query.first(email=email.data)
