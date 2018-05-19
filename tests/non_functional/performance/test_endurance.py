import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_endurance(default_home_request: Request, success: int) -> None:
    t: int = 1000
    c: int = 0
    while True:
        assert default_home_request.response().status_code() == success
        c += 1
        if c == t:
            break
