import pytest

_success: int = 200
_not_found: int = 404
_forbidden: int = 403


@pytest.fixture(scope='module')
def success() -> int:
    """Represent `200` success status code"""

    return _success


@pytest.fixture(scope='module')
def not_found() -> int:
    """Represent `404` success status code"""

    return _not_found


@pytest.fixture(scope='module')
def forbidden() -> int:
    """Represent `403` success status code"""

    return _forbidden
