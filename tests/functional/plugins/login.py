import pytest
from server.api.requests import SafeGetRequest
from server.api.responses import Response

_login_url: str = 'http://localhost:5000/login'


@pytest.fixture(scope='module')
def login_url_response() -> Response:
    """Represent response from `login` page"""

    return SafeGetRequest(_login_url).response()
