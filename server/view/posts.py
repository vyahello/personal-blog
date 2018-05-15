from abc import ABC, abstractmethod
from typing import Dict, List
from datetime import datetime


class Post(ABC):
    """Represent abstraction for a post object."""

    @abstractmethod
    def __call__(self) -> List[Dict[str, str]]:
        pass


class Date(ABC):
    """Represent abstraction for a date."""

    @abstractmethod
    def __call__(self) -> str:
        pass


class PostDate(Date):
    """Represent abstraction for a post date."""

    def __init__(self) -> None:
        self._fmt = '%B %d, %Y'

    def __call__(self) -> str:
        return datetime.strftime(datetime.today(), self._fmt)


class BlogPost(Post):
    """Represent a blog post object."""

    def __init__(self) -> None:
        self._date = PostDate()

    def __call__(self) -> List[Dict[str, str]]:
        return [
            {
                'author': 'Volodymyr Yahello',
                'title': 'Blog Post #1',
                'content': 'Test content',
                'date_posted': f"{self._date()}"
            }
        ]
