from blog.api.responses import Response
from tests.markers import smoke

_zero: int = 0


@smoke
def test_about_page_url(about_url_response: Response, success: int) -> None:
    assert about_url_response.status_code() == success


@smoke
def test_about_page_content(about_url_response: Response) -> None:
    assert len(about_url_response.as_str()) > _zero
