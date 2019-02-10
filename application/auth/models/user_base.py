# -*- coding: utf_8 -*-

import binascii
import os

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from application.modules.bcrypt import bcrypt
from application.modules.db import db


class UserBase(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)


    _password = db.Column("password", db.LargeBinary(60), nullable=True)

    session_token = db.Column(db.String(128), unique=True, nullable=False)


    def __init__(self, *args, **kwargs):
        super(UserBase, self).__init__(*args, **kwargs)

        self.session_token = binascii.hexlify(os.urandom(64)).decode("utf-8")

    def __str__(self):
        return self.username

    def get_id(self):
        return self.session_token

    @property
    def is_active(self):
        return self.active and self.email_checked

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)
