# -*- coding: utf_8 -*-

from flask import render_template
from flask_login.utils import login_required

from ..blueprint import blueprint as bp


@bp.route('/terra')
@login_required
def terra():
    return render_template("terra.html")
