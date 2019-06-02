from marshmallow import fields, post_dump
from flask import request

from application.modules.schema import BaseSchema
from application.terra.models import Transaction


class TransactionSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Transaction

    created = fields.DateTime(dump_only=True)
    status = fields.Boolean(dump_only=True)
