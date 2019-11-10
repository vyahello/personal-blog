import time
from blog.api.requests import Request
from tests.markers import performance

_xtime: int = 1000
_zero: int = 0
_inc: int = 1
_exp_res: int = 12


@performance
def test_stress(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    times: int = _xtime
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
    t2: float = time.time()
    assert t2-t1 < _exp_res
