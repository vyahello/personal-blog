import time
import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_smoke(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    for _ in range(100):
        assert default_home_request.response().status_code() == success
    t2: float = time.time()
    assert t2-t1 < 1
