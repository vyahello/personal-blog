import pytest
from server.api.responses import Response

_success: int = 200
_zero: int = 0


@pytest.mark.smoke
def test_default_home_page_url(default_home_url_response: Response) -> None:
    assert default_home_url_response.status_code() == _success


@pytest.mark.smoke
def test_home_page_url(home_url_response: Response) -> None:
    assert home_url_response.status_code() == _success


@pytest.mark.smoke
def test_default_home_page_content(default_home_url_response: Response) -> None:
    assert len(default_home_url_response.as_str()) > _zero


@pytest.mark.smoke
def test_home_page_content(home_url_response: Response) -> None:
    assert len(home_url_response.as_str()) > _zero
