from abc import ABC, abstractmethod
from typing import Dict, Any

from flask import url_for


class UrlFor(ABC):
    """Represent abstraction of url redirection."""

    @abstractmethod
    def __call__(self) -> str:
        pass


class PageUrlFor(UrlFor):
    """Represent concrete url redirection."""

    def __init__(self, endpoint: str, **options: str) -> None:
        self._endpoint = endpoint
        self._options = options

    def __call__(self) -> str:
        return url_for(self._endpoint, **self._options)
