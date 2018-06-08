import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response

_register: str = '/register'


@pytest.fixture(scope='module')
def register_url_response(url_endpoint: str) -> Response:
    """Represent response from `register` page"""

    return Get(url_endpoint + _register).response()


@pytest.fixture(scope='module')
def register_user_request(url_endpoint: str) -> Request:
    """Represent ``post`` request for `register` page"""

    return Post(url_endpoint + _register)
