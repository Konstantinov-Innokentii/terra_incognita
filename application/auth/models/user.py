from .user_base import UserBase
from application.modules.db.base import *


class User(UserBase):

    fullname = Column(String(1000))
    birthdate = Column(Date)

    isAdmin = Column(Boolean, default=False)

    # def is_admin(self):
    #     return False
