import pytest
from server.api.requests import Request

_xtime: int = 1000
_zero: int = 0
_inc: int = 1


@pytest.mark.performance
def test_endurance(default_home_request: Request, success: int) -> None:
    times: int = _xtime
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
