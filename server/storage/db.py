from abc import ABC, abstractmethod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class DB(ABC):
    """Represent abstraction for a database."""

    @abstractmethod
    def synchronize(self) -> SQLAlchemy:
        pass


class SqlDB(DB):
    """Represent concrete SQL DB."""

    def __init__(self, server: Flask) -> None:
        self._db = SQLAlchemy(server)

    def synchronize(self) -> SQLAlchemy:
        return self._db
