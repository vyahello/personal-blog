from typing import Union
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.server import WebServer
from server.storage.db import SqlDB
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from server.types import Customizable

blog: Union[Flask, Customizable] = WebServer()
blog.customize()
db: SQLAlchemy = SqlDB(blog).synchronize()
bcrypt: Bcrypt = Bcrypt(blog)
login_mng: LoginManager = LoginManager(blog)
login_mng.login_view: str = 'login'
login_mng.login_message_category: str = 'info'

from server import routes
