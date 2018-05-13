from abc import ABC, abstractmethod
from flask import redirect
from server.view.urls import UrlFor


class Redirect(ABC):
    """Represent abstraction of redirection."""

    @abstractmethod
    def link(self) -> str:
        pass


class BlogRedirect(Redirect):
    """Represent concrete redirection."""

    def __init__(self, endpoint: UrlFor) -> None:
        self._endpoint = endpoint

    def link(self) -> str:
        return redirect(self._endpoint())
