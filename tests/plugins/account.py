import pytest
from blog.api.requests import Get
from blog.api.responses import Response

_account: str = '/account'


@pytest.fixture(scope='module')
def account_url_response(url_endpoint: str) -> Response:
    """Represent response from `account` page"""

    return Get(url_endpoint + _account).response()
