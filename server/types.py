from abc import ABC,  abstractmethod


class Customizable(ABC):
    """Represent customizable object."""

    @abstractmethod
    def customize(self) -> None:
        pass


class Action(ABC):
    """Represent abstraction for an object."""

    @abstractmethod
    def perform(self) -> str:
        pass


class Update(Action):
    """Represent object for some save action."""

    pass


class Inform(Action):
    """Represent object for some inform action."""

    pass


class Abort(Action):
    """Represent object for abort action."""

    pass
