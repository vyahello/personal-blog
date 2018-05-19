import time
import pytest
from server.api.requests import Request

_success: int = 200


@pytest.mark.performance
def test_stress(default_home_request: Request, success: int) -> None:
    t1: float = time.time()
    for _ in range(1000):
        assert default_home_request.response().status_code() == success
    t2: float = time.time()
    assert t2-t1 < 10
