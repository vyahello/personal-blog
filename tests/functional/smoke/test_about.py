import pytest
from server.api.responses import Response

_zero: int = 0


@pytest.mark.smoke
def test_about_page_url(about_url_response: Response, success: int) -> None:
    assert about_url_response.status_code() == success


@pytest.mark.smoke
def test_about_page_content(about_url_response: Response) -> None:
    assert len(about_url_response.as_str()) > _zero
