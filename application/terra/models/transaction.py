from datetime import datetime

from flask import request
from sqlalchemy.event import listens_for
from flask_sqlalchemy_session import current_session
from sqlalchemy.orm.attributes import get_history

from application.modules.db.base import *


class Transaction(Base):

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)

    created = Column(DateTime, nullable=False)

    owner_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User", backref=backref("transactions"))

    source = Column(Integer, nullable=False)
    target = Column(Integer, nullable=False)

    status = Column(Boolean)
    value = Column(Integer)

    message = Column(Text, nullable=True)
