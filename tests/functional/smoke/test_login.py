from typing import Dict
from blog.api.requests import Request
from blog.api.responses import Response
from tests.markers import smoke

_zero: int = 0


@smoke
def test_login_page_url(login_url_response: Response, success: int) -> None:
    assert login_url_response.status_code() == success


@smoke
def test_login_page_content(login_url_response: Response) -> None:
    assert len(login_url_response.as_str()) > _zero


@smoke
def test_login_user(login_user_request: Request, success: int) -> None:
    data: Dict[str, str] = {"email": "admin@blog.com", "password": "password", "submit": "Login"}
    assert login_user_request.response(data=data).status_code() == success
