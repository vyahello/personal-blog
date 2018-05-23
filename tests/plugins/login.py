import pytest
from server.api.requests import Get, Request, Post
from server.api.responses import Response


@pytest.fixture(scope='module')
def login_url_response(url_endpoint) -> Response:
    """Represent response from `login` page"""

    return Get(url_endpoint + '/login').response()


@pytest.fixture(scope='module')
def login_user_request(url_endpoint) -> Request:
    """Represent ``post`` request for `login` page"""

    return Post(url_endpoint + '/login')
