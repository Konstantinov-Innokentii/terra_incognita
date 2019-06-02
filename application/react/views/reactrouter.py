# -*- coding: utf_8 -*-

from flask import render_template
from flask_login.utils import login_required

from ..blueprint import blueprint as bp


@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
@login_required
def catch_all(path):
    return render_template("terra.html")
