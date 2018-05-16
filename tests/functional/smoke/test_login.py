import pytest
from server.api.responses import Response

_success: int = 200
_zero: int = 0


@pytest.mark.smoke
def test_login_page(login_url_response: Response) -> None:
    assert login_url_response.status_code() == _success


@pytest.mark.smoke
def test_login_page_content(login_url_response: Response) -> None:
    assert len(login_url_response.as_str()) > _zero
