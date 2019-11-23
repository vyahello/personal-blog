from abc import ABC, abstractmethod
from typing import Any, Callable
from flask_sqlalchemy import SQLAlchemy
from blog.storage.db import DB


class Session(ABC):
    """Represent abstraction database session."""

    @abstractmethod
    def synchronize(self) -> SQLAlchemy:
        pass

    @abstractmethod
    def add(self, data: Any) -> None:
        pass

    @abstractmethod
    def delete(self, data: Any) -> None:
        pass


class UserSession(Session):
    """Represent concrete database session."""

    def __init__(self, db: DB) -> None:
        def _sync() -> SQLAlchemy:
            sync = db.synchronize()
            sync.create_all()
            return sync

        self._db: DB = db
        self._sync: Callable[..., SQLAlchemy] = _sync

    def synchronize(self) -> SQLAlchemy:
        return self._db.synchronize()

    def add(self, data: Any) -> None:
        self._sync().session.add(data)
        self._sync().session.commit()

    def delete(self, data: Any) -> None:
        self._sync().session.delete(data)
        self._sync().session.commit()
