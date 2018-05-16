from abc import ABC, abstractmethod
from requests import Session
from server.api.responses import Response, HttpResponseError, HttpResponse


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self) -> Response:
        pass


class GetRequest(Request):
    """Represent a api ``get`` request."""

    def __init__(self, url: str) -> None:
        self._session: Session = Session()
        self._url: str = url

    def response(self) -> Response:
        return HttpResponse(self._session.get(self._url, verify=False))


class SafeGetRequest(Request):
    """Represent a safe GET request.
    Raise an error if `200` response status code is not presented.
    """

    def __init__(self, url: str, status_code: int = 200) -> None:
        self._req: Request = GetRequest(url)
        self._code: int = status_code

    def response(self) -> Response:
        if self._req.response().status_code() != self._code:
            raise HttpResponseError(
                'HTTP response error with {} status code!!!'.format(self._req.response().status_code()))
        return self._req.response()
