from abc import ABC, abstractmethod
from typing import Any
from flask import render_template
from server.view.posts import Post


class Template(ABC):
    """Represent abstraction of a server template."""

    @abstractmethod
    def render(self, **context: Any) -> str:
        pass


class YFoxTemplate(Template):
    """Represent a blog template."""

    def __init__(self, template: str) -> None:
        self._template = template

    def render(self, **context: Any) -> str:
        return render_template(self._template, **context)


class YFoxTemplatePosts(Template):
    """Represent a blog template with posts."""

    def __init__(self, template: str) -> None:
        self._template = YFoxTemplate(template)

    def render(self, posts: Post) -> str:
        return self._template.render(posts=posts())
