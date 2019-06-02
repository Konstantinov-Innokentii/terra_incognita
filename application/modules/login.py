# -*- coding: utf_8 -*-

from flask_login import LoginManager
from flask_sqlalchemy_session import current_session

from application.api.v1 import blueprint as api_v1_bp


login_manager = LoginManager()

login_manager.login_view = "auth.signin"

login_manager.blueprint_login_views = {
    api_v1_bp.name: None,
}


@login_manager.user_loader
def load_user(id):
    from application.auth.models import User
    return current_session.query(User).filter(User.session_token == id).first()
