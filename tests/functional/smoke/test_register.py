from typing import Dict
import pytest
from server.api.requests import Request
from server.api.responses import Response

_zero: int = 0


@pytest.mark.smoke
def test_register_page_url(register_url_response: Response, success: int) -> None:
    assert register_url_response.status_code() == success


@pytest.mark.smoke
def test_register_page_content(register_url_response: Response) -> None:
    assert len(register_url_response.as_str()) > _zero


@pytest.mark.smoke
def test_register_user(register_user_request: Request, success: int) -> None:
    data: Dict[str, str] = {"username": "vyah@blog.com",
                            "password": "password",
                            "confirm_password": "password",
                            "submit": "Sing+Up"}

    assert register_user_request.response(data=data).status_code() == success
