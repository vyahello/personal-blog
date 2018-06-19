from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from server import db, login_mng
from flask_login import UserMixin
from server.storage.sessions import UserSession


_db: SQLAlchemy = UserSession(db).synchronize()
_pic: str = 'default.jpg'


class User(_db.Model, UserMixin):
    """Represent user model."""

    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(20), unique=True, nullable=False)
    email = _db.Column(_db.String(120), unique=True, nullable=False)
    image_file = _db.Column(_db.String(20), nullable=False, default=_pic)
    password = _db.Column(_db.String(60), nullable=False)
    posts = _db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', {self.image_file})"


class Post(_db.Model):
    """Represent post model."""

    id = _db.Column(_db.Integer, primary_key=True)
    title = _db.Column(_db.String(1000), nullable=False)
    date_posted = _db.Column(_db.DateTime, nullable=False, default=datetime.utcnow)
    content = _db.Column(_db.Text, nullable=False)
    user_id = _db.Column(_db.Integer, _db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Post('{self.title}', '{self.date_posted}')"


@login_mng.user_loader
def load_user(user_id: str) -> User:
    return User.query.get(int(user_id))
