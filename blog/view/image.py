import os
import secrets
from typing import Tuple
from PIL import Image
from flask_wtf import FlaskForm
from blog import WebServer
from blog.types import Update


class UpdateImage(Update):
    """Update user image."""

    def __init__(self, form_picture: FlaskForm, blog: WebServer) -> None:
        self._form = form_picture
        self._blog = blog
        self._image = Image
        self._res: Tuple[int, int] = (125, 125)
        self._pic_path: str = "static/accounts"

    def perform(self) -> str:
        data = self._form.picture.data
        random_hex: str = secrets.token_hex(8)
        _, f_ext = os.path.splitext(data.filename)
        picture_fn: str = random_hex + f_ext
        picture_path: str = os.path.join(self._blog.root_path, self._pic_path, picture_fn)
        output_size: Tuple[int, int] = self._res
        image: Image = self._image.open(data)
        image.thumbnail(output_size)
        image.save(picture_path)
        return picture_fn
