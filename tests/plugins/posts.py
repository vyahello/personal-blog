import pytest
from server.api.requests import Get
from server.api.responses import Response

_new_post: str = '/post/new'
_exist_post_id: str = '/post/4'
_non_exist_post_id: str = '/post/NONE'
_update_post: str = '/update'


@pytest.fixture(scope='module')
def new_post(url_endpoint: str) -> Response:
    """Represent response from ``new post`` page."""

    return Get(url_endpoint + _new_post).response()


@pytest.fixture(scope='module')
def existent_post_response(url_endpoint: str) -> Response:
    """Represent response from existent post"""

    return Get(url_endpoint + _exist_post_id).response()


@pytest.fixture(scope='module')
def non_existent_post_response(url_endpoint: str) -> Response:
    """Represent response from non existent post."""

    return Get(url_endpoint + _non_exist_post_id).response()


@pytest.fixture(scope='module')
def update_existent_post_response(url_endpoint: str) -> Response:
    """Represent response from ``update`` post page with existent post."""

    return Get(url_endpoint + _exist_post_id + _update_post).response()


@pytest.fixture(scope='module')
def update_non_existent_post_response(url_endpoint: str) -> Response:
    """Represent response from ``update`` post page with non existent post."""

    return Get(url_endpoint + _non_exist_post_id + _update_post).response()
