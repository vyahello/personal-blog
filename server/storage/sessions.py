from abc import ABC, abstractmethod
from flask_sqlalchemy import SQLAlchemy
from server.storage.db import DB


class Session(ABC):
    """Represent abstraction database session."""

    @abstractmethod
    def synchronize(self) -> SQLAlchemy:
        pass

    @abstractmethod
    def add(self, user) -> None:
        pass


class UserSession(Session):
    """Represent concrete database session."""

    def __init__(self, db: DB) -> None:

        def add_user(user) -> None:
            sync = db.synchronize()
            sync.create_all()
            sync.session.add(user)
            sync.session.commit()

        self._db = db
        self._add_user = add_user

    def synchronize(self) -> SQLAlchemy:
        return self._db.synchronize()

    def add(self, user) -> None:
        self._add_user(user)
