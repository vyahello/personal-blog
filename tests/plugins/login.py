import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response

_login: str = '/login'


@pytest.fixture(scope='module')
def login_url_response(url_endpoint: str) -> Response:
    """Represent response from `login` page"""

    return Get(url_endpoint + _login).response()


@pytest.fixture(scope='module')
def login_user_request(url_endpoint: str) -> Request:
    """Represent ``post`` request for `login` page"""

    return Post(url_endpoint + _login)
