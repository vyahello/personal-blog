from abc import ABC, abstractmethod
from flask import Flask
from flask_sslify import SSLify


class SSLCertificate(ABC):
    """Represent abstraction for ssl certificate."""

    @abstractmethod
    def verify(self) -> SSLify:
        pass


class FlaskSSL(SSLCertificate):
    """Represent flask `ssl` certificate."""

    def __init__(self, server: Flask) -> None:
        self._ssl: SSLify = SSLify(server)

    def verify(self) -> SSLify:
        return self._ssl
