from server.server import WebServer
from server.storage.db import SqlDB
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

blog = WebServer()
blog.customize()
db = SqlDB(blog).synchronize()
bcrypt = Bcrypt(blog)
login_mng = LoginManager(blog)
login_mng.login_view = 'login'
login_mng.login_message_category = 'info'

from server import routes
