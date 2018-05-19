import time
import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_load(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    for _ in range(500):
        assert default_home_request.response().status_code() == success
    t2: float = time.time()
    assert t2-t1 < 5
