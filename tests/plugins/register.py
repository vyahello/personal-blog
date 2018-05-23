import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response

_register_url: str = 'http://localhost:5000/register'


@pytest.fixture(scope='module')
def register_url_response(url_endpoint) -> Response:
    """Represent response from `register` page"""

    return Get(url_endpoint + '/register').response()


@pytest.fixture(scope='module')
def register_user_request(url_endpoint) -> Request:
    """Represent ``post`` request for `register` page"""

    return Post(url_endpoint + '/register')
