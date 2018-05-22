from abc import ABC, abstractmethod
from flask import flash


class Flash(ABC):
    """Represent abstraction of flash."""

    @abstractmethod
    def display(self) -> str:
        pass


class PageFlash(Flash):
    """Represent a flash for a particular event ."""

    def __init__(self, message: str, event: str) -> None:
        self._message = message
        self._event = event

    def display(self) -> str:
        return flash(self._message, self._event)
