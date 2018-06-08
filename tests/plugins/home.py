import pytest
from server.api.requests import Get, Request
from server.api.responses import Response

_home: str = '/home'


@pytest.fixture(scope='module')
def default_home_url_response(url_endpoint: str) -> Response:
    """Represent response from `default home` page"""

    return Get(url_endpoint).response()


@pytest.fixture(scope='module')
def home_url_response(url_endpoint: str) -> Response:
    """Represent response from `home` page"""

    return Get(url_endpoint + _home).response()


@pytest.fixture(scope='module')
def default_home_request(url_endpoint: str) -> Request:
    """Represent request for `default home` page"""

    return Get(url_endpoint)
