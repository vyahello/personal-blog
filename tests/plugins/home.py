import pytest
from server.api.requests import Get, Request
from server.api.responses import Response


@pytest.fixture(scope='module')
def default_home_url_response(url_endpoint) -> Response:
    """Represent response from `default home` page"""

    return Get(url_endpoint).response()


@pytest.fixture(scope='module')
def home_url_response(url_endpoint) -> Response:
    """Represent response from `home` page"""

    return Get(url_endpoint + '/home').response()


@pytest.fixture(scope='module')
def default_home_request(url_endpoint) -> Request:
    """Represent request for `default home` page"""

    return Get(url_endpoint)
