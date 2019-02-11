# -*- coding: utf_8 -*-

from flask_sqlalchemy_session import flask_scoped_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SessionFactory(object):

    app = None
    session = None

    def __init__(self, app=None):
        super(SessionFactory, self).__init__()

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.session = flask_scoped_session(self.session_factory, app)

    @property
    def session_factory(self):
        self.engine = create_engine(self.app.config['DATABASE_URL'],
                                    echo=self.app.config['DEBUG'] and self.app.config.get('DATABASE_DEBUG_SQL', False))
        return sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def create_session(self):
        assert self.app
        return self.session_factory()
