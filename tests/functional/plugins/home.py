import pytest
from server.api.requests import SafeGetRequest
from server.api.responses import Response

_default_home_url: str = 'http://localhost:5000'
_home_url: str = 'http://localhost:5000/home'


@pytest.fixture(scope='module')
def default_home_url_response() -> Response:
    """Represent response from `default home` page"""

    return SafeGetRequest(_default_home_url).response()


@pytest.fixture(scope='module')
def home_url_response() -> Response:
    """Represent response from `home` page"""

    return SafeGetRequest(_home_url).response()
