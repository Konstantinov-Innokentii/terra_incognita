from .user_base import UserBase
from application.modules.db import db


class User(UserBase):

    __tablename__ = None

    fullname = db.Column(db.String(1000))
    birthdate = db.Column(db.Date)

    def is_admin(self):
        return False
