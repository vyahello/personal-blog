import time
from server.api.requests import Request
from tests.markers import performance

_xtime: int = 500
_zero: int = 0
_exp_res: int = 7
_inc: int = 1


@performance
def test_load(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    times: int = _xtime
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
    t2: float = time.time()
    assert t2-t1 < _exp_res
