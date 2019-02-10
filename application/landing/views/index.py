# -*- coding: utf_8 -*-

from flask import render_template

from ..blueprint import blueprint as bp


@bp.route('/')
def index():
    return render_template("index.html")
