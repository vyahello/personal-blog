from server.api.responses import Response
from tests.markers import smoke


@smoke
def test_new_post(new_post: Response, success: int) -> None:
    assert new_post.status_code() == success


@smoke
def test_existent_post(existent_post_response: Response, success: int) -> None:
    assert existent_post_response.status_code() == success


@smoke
def test_non_existent_post(non_existent_post_response: Response, not_found: int) -> None:
    assert non_existent_post_response.status_code() == not_found


@smoke
def test_update_existent_post(update_existent_post_response: Response, success: int) -> None:
    assert update_existent_post_response.status_code() == success


@smoke
def test_update_non_existent_post(update_non_existent_post_response: Response, not_found: int) -> None:
    assert update_non_existent_post_response.status_code() == not_found
