from flask import request, abort
from flask_login.utils import login_required, current_user
from flask_restful import Resource
from flask_sqlalchemy_session import current_session
from sqlalchemy.sql.expression import or_

from application.api import api_v1
from application.auth.models import User

# from application.terra.models import Account
# from application.terra.schemas import AccountSchema
#
# accounts_schema = AccountSchema(many=True)


from application.auth.schemas.user import UserSchema, UserSchemaCreate

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserResource(Resource):

    @login_required
    def get(self, id):
        user = current_session.query(User).get(id)
        return user_schema.dump(user).data

    @login_required
    def put(self, id):
        assert request.json["id"] == id

        if id != current_user.id:
            abort(401)

        user = user_schema.load(request.json)
        current_session.add(user.data)
        current_session.commit()
        return user_schema.dump(user.data).data, 201


class UserListResource(Resource):


    @login_required
    def get(self):
        users = current_session.query(User)

        if "email" in request.args:
            users = users.filter(or_(
                User.username.startswith(request.args["email"]),
                User.email.startswith(request.args["email"])
            ))

        return users_schema.dump(users).data

    @login_required
    def post(self):
        user = UserSchemaCreate().load(request.json).data
        current_session.add(user)
        current_session.commit()

        return user_schema.dump(user).data, 201


api_v1.add_resource(UserListResource, '/user')
api_v1.add_resource(UserResource, '/user/<int:id>')
