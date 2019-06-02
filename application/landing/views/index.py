# -*- coding: utf_8 -*-

from flask import render_template, redirect, url_for, session
from flask_login.utils import current_user

from ..blueprint import blueprint as bp


@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("react.terra"))

    from application.auth.forms import RegistrationForm
    form = RegistrationForm()
    return render_template("index.html", form=form)
