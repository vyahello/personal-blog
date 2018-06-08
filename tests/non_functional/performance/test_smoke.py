import time
import pytest
from server.api.requests import Request

_xtime: int = 100
_zero: int = 0
_inc: int = 1
_exp_res: int = 2


@pytest.mark.performance
def test_smoke(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    times: int = _xtime
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
    t2: float = time.time()
    assert t2-t1 < _exp_res
