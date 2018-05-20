import time
import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_load(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    times: int = 500
    while times > 0:
        assert default_home_request.response().status_code() == success
        times -= 1
    t2: float = time.time()
    print(t2-t1)
    assert t2-t1 < 5
