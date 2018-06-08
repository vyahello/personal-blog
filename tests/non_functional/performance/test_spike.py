import time
from typing import List
import pytest
from server.api.requests import Request

_xtime: int = 500
_step: List[int] = [200, 400, 600, 800]
_zero: int = 0
_inc: int = 1
_sleep: int = 7


@pytest.mark.performance
def test_spike(default_home_request: Request, success: int) -> None:
    times: int = _xtime
    step: List[int] = _step
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
        if times in step:
            time.sleep(_sleep)
