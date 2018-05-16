import pytest
from server.api.requests import SafeGetRequest
from server.api.responses import Response

_register_url: str = 'http://localhost:5000/register'


@pytest.fixture(scope='module')
def register_url_response() -> Response:
    """Represent response from `response` page"""

    return SafeGetRequest(_register_url).response()
