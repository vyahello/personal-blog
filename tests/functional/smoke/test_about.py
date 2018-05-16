import pytest
from server.api.responses import Response

_success: int = 200
_zero: int = 0


@pytest.mark.smoke
def test_about_page(about_url_response: Response) -> None:
    assert about_url_response.status_code() == _success


@pytest.mark.smoke
def test_about_content(about_url_response: Response) -> None:
    assert len(about_url_response.as_str()) > _zero
