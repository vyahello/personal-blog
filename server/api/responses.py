from abc import ABC, abstractmethod
from typing import Dict, Any
import requests


class Response(ABC):
    """The abstraction of a response from an api request."""

    @abstractmethod
    def status_code(self) -> str:
        pass

    @abstractmethod
    def as_str(self) -> str:
        pass

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass


class HttpResponseError(Exception):
    """Represent http response error object."""

    pass


class HttpResponse(Response):
    """Represent an HTTP response from an api request."""

    def __init__(self, response: requests.Response) -> None:
        self._response: requests.Response = response

    def status_code(self) -> int:
        return self._response.status_code

    def as_str(self) -> str:
        return str(self._response.content)

    def as_dict(self) -> Dict[Any, Any]:
        return self._response.json()
