import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response

_register_url: str = 'http://localhost:5000/register'


@pytest.fixture(scope='module')
def register_url_response() -> Response:
    """Represent response from `register` page"""

    return Get(_register_url).response()


@pytest.fixture(scope='module')
def register_user_request() -> Request:
    """Represent ``post`` request for `register` page"""

    return Post(_register_url)
