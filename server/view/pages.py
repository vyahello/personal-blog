from abc import ABC, abstractmethod
from flask import flash, redirect, request, url_for, abort
from werkzeug.local import LocalProxy
from server.types import Inform


class UrlFor(ABC):
    """Represent abstraction of url redirection."""

    @abstractmethod
    def __call__(self) -> str:
        pass


class Flash(ABC):
    """Represent abstraction of flash."""

    @abstractmethod
    def display(self) -> str:
        pass


class Redirect(ABC):
    """Represent abstraction of redirection."""

    @abstractmethod
    def link(self) -> str:
        pass


class Request(ABC):
    """Represent abstraction of request redirection."""

    @abstractmethod
    def get(self) -> str:
        pass

    @abstractmethod
    def method(self) -> str:
        pass


class Abort(ABC):
    """Represent abstraction for abort action."""

    @abstractmethod
    def perform(self) -> str:
        pass


class AbortPage(Abort):
    """Represent abort page."""

    def __init__(self, code: int) -> None:
        self._code = code

    def perform(self) -> str:
        return abort(self._code)


class PageUrlFor(UrlFor):
    """Represent concrete url redirection."""

    def __init__(self, endpoint: str, **options: str) -> None:
        self._endpoint = endpoint
        self._options = options

    def __call__(self) -> str:
        return url_for(self._endpoint, **self._options)


class PageFlash(Flash):
    """Represent a flash for a particular event ."""

    def __init__(self, message: str, event: str) -> None:
        self._message = message
        self._event = event

    def display(self) -> str:
        return flash(self._message, self._event)


class PageRedirect(Redirect):
    """Represent concrete redirection."""

    def __init__(self, endpoint: UrlFor) -> None:
        self._endpoint = endpoint

    def link(self) -> str:
        return redirect(self._endpoint())


class PageRequest(Request):
    """Represent next request page."""

    def __init__(self, page: str = '') -> None:
        self._page: str = page
        self._req: LocalProxy = request

    def method(self) -> str:
        return self._req.method

    def get(self) -> str:
        return self._req.args.get(self._page)


class InformPage(Inform):
    """Inform about page actions."""

    def __init__(self, message: str, outcome: str, path: str, **options: str) -> None:
        self._flash = PageFlash(message, outcome)
        self._red = PageRedirect(PageUrlFor(path, **options))

    def outcome(self) -> str:
        self._flash.display()
        return self._red.link()
