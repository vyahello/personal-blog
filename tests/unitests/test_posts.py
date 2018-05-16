import pytest
from datetime import datetime
from server.view.posts import PostDate, BlogPost

_fmt = '%B %d, %Y'


@pytest.fixture(scope="module")
def date() -> str:
    return datetime.strftime(datetime.today(), _fmt)


@pytest.mark.unittest
def test_post_date(date: str) -> None:
    pdate = PostDate()
    assert date == pdate()


@pytest.mark.unittest
def test_blog_post(date: str) -> None:
    post = BlogPost()
    assert post() == [
            {
                'author': 'Volodymyr Yahello',
                'title': 'Blog Post #1',
                'content': 'Test content',
                'date_posted': f"{date}"
            }
        ]
