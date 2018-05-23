import pytest


@pytest.fixture(scope='module')
def url_endpoint() -> str:
    """Represent default url endpoint."""

    return 'http://localhost:5000'
