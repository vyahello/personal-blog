from typing import Union
from flask import Flask
from blog.server import WebServer
from blog.storage.db import SqlDB, DB
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.types import Customizable

yfox: Union[Flask, Customizable] = WebServer()
yfox.customize()
db: DB = SqlDB(yfox)
bcrypt: Bcrypt = Bcrypt(yfox)
login_mng: LoginManager = LoginManager(yfox)
login_mng.login_view: str = 'login'
login_mng.login_message_category: str = 'info'

from blog import routes
