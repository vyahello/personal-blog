from abc import ABC, abstractmethod


class Customizable(ABC):
    """Represent customizable object."""

    @abstractmethod
    def customize(self) -> None:
        pass
