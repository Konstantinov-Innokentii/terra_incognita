from flask import request, abort
from flask_login.utils import login_required, current_user
from flask_restful import Resource
from flask_sqlalchemy_session import current_session


from application.api import api_v1
from application.terra.models import Account
from application.terra.schemas import AccountSchema

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)


class AccountResource(Resource):

    @login_required
    def get(self, id):
        account = current_session.query(Account).get(id)
        assert account.owner_id == current_user.id

        return account_schema.dump(account).data

    @login_required
    def delete(self, id):
        account = current_session.query(Account).get(id)
        assert account.owner_id == current_user.id
        current_session.delete(account)
        current_session.commit()
        return '', 204

    @login_required
    def put(self, id):
        assert request.json["id"] == id

        account = account_schema.load(request.json, partial=True)
        assert account.owner_id == current_user.id

        current_session.add(account.data)
        current_session.commit()
        return account_schema.dump(account.data).data, 201

class AccountListResource(Resource):

    # @login_required
    def get(self):
        profile_id = request.args.get('profile_id', None)
        # assert int(profile_id) == current_user.id
        if profile_id is None:
            return []
        accounts = current_session.query(Account).filter(Account.owner_id == int(profile_id))
        return accounts_schema.dump(accounts).data

    @login_required
    def post(self):
        account = Account()
        account.owner = current_user
        current_session.add(account)
        current_session.commit()
        return account_schema.dump(account).data, 201


api_v1.add_resource(AccountListResource, '/account')
api_v1.add_resource(AccountResource, '/account/<int:id>')
