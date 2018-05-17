from abc import ABC, abstractmethod
from typing import Dict, Any

from requests import Session
from server.api.responses import Response, HttpResponseError, HttpResponse


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self, **kwargs: Dict[Any, Any]) -> Response:
        pass


class Get(Request):
    """Represent an api ``get`` request."""

    def __init__(self, url: str) -> None:
        self._session: Session = Session()
        self._url: str = url

    def response(self, **kwargs: Dict[Any, Any]) -> Response:
        return HttpResponse(self._session.get(self._url, **kwargs, verify=False))


class Post(Request):
    """Represent an api ``post`` request."""

    def __init__(self, url: str) -> None:
        self._session: Session = Session()
        self._url: str = url

    def response(self, **kwargs: Dict[Any, Any]) -> Response:
        return HttpResponse(self._session.post(self._url, kwargs, verify=False))


class SafeRequest(Request):
    """Represent a safe request.
    Raise an error if specific status code is not presented.
    """

    def __init__(self, req: Request, status_code: int = 200) -> None:
        self._req: Request = req
        self._code: int = status_code

    def response(self, **kwargs: Dict[Any, Any]) -> Response:
        if self._req.response().status_code() != self._code:
            raise HttpResponseError(
                'HTTP response error with {} status code!!!'.format(self._req.response().status_code()))
        return self._req.response()
