import pytest
from server.api.requests import Get
from server.api.responses import Response


@pytest.fixture(scope='module')
def about_url_response(url_endpoint) -> Response:
    """Represent response from `about` page"""

    return Get(url_endpoint + '/about').response()
