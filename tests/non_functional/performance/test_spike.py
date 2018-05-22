import time
from typing import List
import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_spike(default_home_request: Request, success: int) -> None:
    times: int = 1000
    step: List[int] = [200, 400, 600, 800]
    while times > 0:
        assert default_home_request.response().status_code() == success
        times -= 1
        if times in step:
            time.sleep(7)
