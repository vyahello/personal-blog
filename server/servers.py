from abc import ABC, abstractmethod
from typing import Any, Callable
from flask import Flask


class Server(ABC):
    """Represent abstraction for a server."""

    @abstractmethod
    def route(self, rule: str, **options: Any) -> Callable[..., Any]:
        pass

    @abstractmethod
    def run(self, host: str = None, port: int = None, debug: Any = None, **options: Any) -> None:
        pass

    @abstractmethod
    def config(self) -> None:
        pass


class WebServer(Server):
    """Represent web server."""

    def __init__(self, name: str = __name__) -> None:
        self._app: Flask = Flask(name)

    def route(self, rule: str, **options: Any) -> Callable[..., Any]:
        return self._app.route(rule, **options)

    def run(self, host: str = None, port: int = None, debug: Any = None, **options: Any) -> None:
        return self._app.run(host, port, debug, **options)

    def config(self) -> None:
        self._app.config['SECRET_KEY']: dict = '162733453f65d810e82eb8d5a53e898b'
