from abc import ABC, abstractmethod


class Customizable(ABC):
    """Represent customizable object."""

    @abstractmethod
    def customize(self) -> None:
        pass


class Update(ABC):
    """Represent abstraction for some save action."""

    @abstractmethod
    def save(self) -> str:
        pass


class Inform(ABC):
    """Represent abstraction for some inform action."""

    @abstractmethod
    def outcome(self) -> str:
        pass