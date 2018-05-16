import pytest
from server.api.responses import Response

_success: int = 200
_zero: int = 0


@pytest.mark.smoke
def test_register_page(register_url_response: Response) -> None:
    assert register_url_response.status_code() == _success


@pytest.mark.smoke
def test_register_page_content(register_url_response: Response) -> None:
    assert len(register_url_response.as_str()) > _zero
