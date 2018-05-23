import pytest
from server.api.requests import Get
from server.api.responses import Response


@pytest.fixture(scope='module')
def account_url_response(url_endpoint) -> Response:
    """Represent response from `account` page"""

    return Get(url_endpoint + '/account').response()
