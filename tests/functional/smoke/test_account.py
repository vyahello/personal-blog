import pytest
from server.api.responses import Response

_zero: int = 0


@pytest.mark.smoke
def test_account_page_url(account_url_response: Response, success: int) -> None:
    assert account_url_response.status_code() == success


@pytest.mark.smoke
def test_account_page_content(account_url_response: Response) -> None:
    assert len(account_url_response.as_str()) > _zero
