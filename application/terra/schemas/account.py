from marshmallow import fields, post_dump
from flask import request

from application.modules.schema import BaseSchema
from application.terra.models import Account


class AccountSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Account

    created = fields.DateTime(dump_only=True)
