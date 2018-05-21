import pytest
from server.api.requests import Request


@pytest.mark.performance
def test_endurance(default_home_request: Request, success: int) -> None:
    times: int = 1000
    while times > 0:
        assert default_home_request.response().status_code() == success
        times -= 1
