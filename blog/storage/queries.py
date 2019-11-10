from abc import ABC, abstractmethod
from typing import Dict
from wtforms import ValidationError
from blog.storage.models import User


class Query(ABC):
    """Represent abstraction for some sql query."""

    @abstractmethod
    def first(self, **content: Dict[str, str]) -> None:
        pass


class UserQuery(Query):
    """Represent user query."""

    def __init__(self, query: User) -> None:
        self._query: User = query

    def first(self, **content: Dict[str, str]) -> None:
        if self._query.filter_by(**content).first():
            raise ValidationError('That field is taken. Please choose different one')
