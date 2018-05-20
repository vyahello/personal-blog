import time
from typing import List
import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_spike(default_home_request: Request, success: int) -> None:
    c: int = 0
    stamp: List[int] = [200, 400, 600, 800]
    while True:
        assert default_home_request.response().status_code() == success
        c += 1
        if c in stamp:
            time.sleep(10)
        if c == 1000:
            break
