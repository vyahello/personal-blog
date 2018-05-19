import pytest

_success: int = 200


@pytest.fixture(scope='module')
def success() -> int:
    """Represent `200` success status code"""

    return _success
