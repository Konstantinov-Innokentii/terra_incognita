from flask import request, abort
from flask_login.utils import login_required, current_user
from flask_restful import Resource
from flask_sqlalchemy_session import current_session
from application.api import api_v1
from application.terra.models import Transaction, Account
from application.terra.schemas import TransactionSchema
import datetime

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)


class TransactionResource(Resource):

    @login_required
    def get(self, id):
        transaction = current_session.query(Transaction).get(id)
        assert transaction.owner_id == current_user.id
        return transaction_schema.dump(transaction).data

    @login_required
    def delete(self, id):
        transaction = current_session.query(Transaction).get(id)
        assert transaction.owner_id == current_user.id
        current_session.delete(transaction)
        current_session.commit()
        return '', 204

    @login_required
    def put(self, id):
        assert request.json["id"] == id
        transaction = transaction_schema.load(request.json, partial=True)
        assert transaction.owner_id == current_user.id
        current_session.add(transaction.data)
        current_session.commit()
        return transaction_schema.dump(transaction.data).data, 201


class TransactionListResource(Resource):

    @login_required
    def get(self):
        profile_id = request.args.get('profile_id', None)
        assert int(profile_id) == current_user.id
        transactions = current_session.query(Transaction).filter(Transaction.owner_id == profile_id)
        return transactions_schema.dump(transactions).data

    @login_required
    def post(self):
        transaction = transaction_schema.load(request.json).data
        transaction.created = datetime.datetime.utcnow()
        transaction.owner = current_user
        source_account = current_session.query(Account).filter_by(number=transaction.source).first()
        target_account = current_session.query(Account).filter_by(number=transaction.target).first()

        if not target_account:
            transaction.status = False
        elif source_account.balance >= transaction.value:
            transaction.status = True
            source_account.balance = source_account.balance - transaction.value
            target_account.balance = target_account.balance + transaction.value
        elif source_account.balance < transaction.value:
            transaction.status = False

        current_session.add(transaction)
        current_session.commit()
        return transaction_schema.dump(transaction).data, 201


api_v1.add_resource(TransactionListResource, '/transaction')
api_v1.add_resource(TransactionResource, '/transaction/<int:id>')
