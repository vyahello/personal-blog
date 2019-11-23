import pytest

_endpoint: str = "http://localhost:5000"


@pytest.fixture(scope="module")
def url_endpoint() -> str:
    """Represent default url endpoint."""

    return _endpoint
