from abc import ABC, abstractmethod
from flask import url_for


class UrlFor(ABC):
    """Represent abstraction of url redirection."""

    @abstractmethod
    def trace(self) -> str:
        pass


class BlogUrlFor(UrlFor):
    """Represent concrete url redirection."""

    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint

    def trace(self) -> str:
        return url_for(self._endpoint)
