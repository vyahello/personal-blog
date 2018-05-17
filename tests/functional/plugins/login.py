import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response

_login_url: str = 'http://localhost:5000/login'


@pytest.fixture(scope='module')
def login_url_response() -> Response:
    """Represent response from `login` page"""

    return Get(_login_url).response()


@pytest.fixture(scope='module')
def login_user_request() -> Request:
    """Represent ``post`` request for `login` page"""

    return Post(_login_url)
