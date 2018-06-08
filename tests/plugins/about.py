import pytest
from server.api.requests import Get
from server.api.responses import Response

_about: str = '/about'


@pytest.fixture(scope='module')
def about_url_response(url_endpoint: str) -> Response:
    """Represent response from `about` page"""

    return Get(url_endpoint + _about).response()
