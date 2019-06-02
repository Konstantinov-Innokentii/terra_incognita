from marshmallow import fields

from application.modules.schema import BaseSchema
from application.auth.models import User


class UserSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = User
        exclude = [
            '_password',
            'session_token',
            'email_checked',
        ]

    username = fields.String()
    email = fields.String(dump_only=True)

    birthdate = fields.Date(allow_none=True)


class UserSchemaCreate(UserSchema):
    email = fields.String()
