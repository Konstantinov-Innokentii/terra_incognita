# -*- coding: utf_8 -*-

from flask import Blueprint
# from flask_login import current_user


blueprint = Blueprint('auth', __name__, template_folder="templates")


# @blueprint.app_context_processor
# def inject_user():
#     from .schemas.user import UserSchema
#     return {
#         "user": UserSchema().dump(current_user).data if current_user.is_authenticated else {},
#     }
