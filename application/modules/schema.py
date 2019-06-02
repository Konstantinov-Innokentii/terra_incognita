from flask_sqlalchemy_session import current_session
from marshmallow_sqlalchemy import ModelSchema


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = current_session

    def handle_error(self, exc, data):
        raise exc
