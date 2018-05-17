from server.server import WebServer
from server.storage.db import SqlDB

blog = WebServer()
blog.customize()
db = SqlDB(blog).synchronize()

from server import routes
