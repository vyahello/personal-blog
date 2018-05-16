import pytest
from server.api.requests import SafeGetRequest
from server.api.responses import Response

_about_url: str = 'http://localhost:5000/about'


@pytest.fixture(scope='module')
def about_url_response() -> Response:
    """Represent response from `about` page"""

    return SafeGetRequest(_about_url).response()
