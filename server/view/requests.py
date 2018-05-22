from abc import ABC, abstractmethod
from flask import request
from werkzeug.local import LocalProxy


class Request(ABC):
    """Represent abstraction of request redirection."""

    @abstractmethod
    def get(self) -> str:
        pass


class NextPageRequest(Request):
    """Represent next request page."""

    def __init__(self, page: str) -> None:
        self._page: str = page
        self._req: LocalProxy = request

    def get(self) -> str:
        return self._req.args.get(self._page)
