from datetime import datetime
import random

from application.modules.db.base import *


class Account(Base):

    __tablename__ = "account"

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)

        self.created = datetime.utcnow()
        self.number = random.randint(1, 1000)
        self.balance = random.randint(1, 1000)

    id = Column(Integer, primary_key=True)

    created = Column(DateTime, nullable=False,)

    owner_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User", backref=backref("accounts"))

    balance = Column(Float, default=0)
    number = Column(Integer, unique=True)

