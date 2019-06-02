from flask import request
import psycopg2
from flask_login.utils import current_user, login_required
from config import DATABASE_URL

from urllib.parse import urlparse

conn_str = urlparse(DATABASE_URL)

username = conn_str.username
password = conn_str.password
database = conn_str.path[1:]
hostname = conn_str.hostname
conn = psycopg2.connect(
    database=database,
    user=username,
    password=password,
    host=hostname
)

cur = conn.cursor()


from ..blueprint import blueprint as bp


@login_required
@bp.route("/get_accounts/<profile>", methods=['GET'])
def get_accounts(profile):
    query = f"SELECT * FROM account WHERE owner_id={profile} AND owner_id={current_user.id}"
    cur.execute(query)
    rows = cur.fetchall()
    return str(list(
        map(lambda row: {'id': row[0], 'created': row[1], 'owner_id': row[2], 'balance': row[3], 'number': row[4]},
            rows)))


@login_required
@bp.route("/get_transaction/<id>", methods=['GET'])
def get_transaction(id):
    query = f"SELECT * FROM transaction t WHERE t.id={id} AND t.owner_id={current_user.id}"
    cur.execute(query)
    try:
        rows = cur.fetchall()
    except psycopg2.ProgrammingError:
        conn.commit()
        return "[]"
    return str(list(
        map(lambda row: {'id': row[0], 'created': row[1], 'owner_id': row[2], 'source': row[3], 'target': row[4]},
            rows)))


@login_required
@bp.route("/get_users_info", methods=['GET'])
def get_users_info():
    if request.args.get('is_admin', None):
        query = f'SELECT username, email FROM "user"'
        cur.execute(query)
        rows = cur.fetchall()
        return str(list(
            map(lambda row: {'username': row[0], 'email': row[1]},
                rows)))

    return 'is_admin?'

