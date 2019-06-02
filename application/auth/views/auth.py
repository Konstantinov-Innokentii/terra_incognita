# -*- coding: utf_8 -*-

from flask import redirect, url_for, render_template, request, flash, current_app, abort, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy_session import current_session
from sqlalchemy.orm.exc import NoResultFound
from urllib.parse import urlparse, urljoin

from application.auth.forms.auth import SignInForm, RegistrationForm
from ..schemas.user import UserSchema
from ..blueprint import blueprint as bp

from ..models import User


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def redirect_back(endpoint, **values):
    target = request.args.get('next', None)
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)


@bp.route('/signin', methods=["GET", "POST"])
def signin():

    if current_user.is_authenticated:
        return redirect(url_for('landing.index'))

    form = SignInForm()

    if request.method == "POST" and form.validate_on_submit():
        try:
            if "@" in form.username.data:
                user = current_session.query(User).filter(User.email == form.username.data).one()
            else:
                user = current_session.query(User).filter(User.username == form.username.data).one()
        except NoResultFound:
            flash("Invalid credentials!")
            return redirect(url_for('auth.signin'))

        if user.is_correct_password(form.password.data):
            if login_user(user):
                return redirect_back('react.terra')
            else:
                flash("Can't sign in!")
        else:
            flash("Invalid credentials!")

    else:
        for error in form.errors:
            """form.errors это list, берется его нулевой элемент,
             в котором лежит сообщение об ошибке, заданное в форме"""
            flash(form.errors[error][0])

    return render_template('signin.html', form=form)


@bp.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect('/auth/signin')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('landing.index'))

    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            current_session.add(user)
            current_session.commit()

            return redirect(url_for('auth.signin'))
        else:
            for error in form.errors:
                """form.errors это list, берется его нулевой элемент,
                 в котором лежит сообщение об ошибке, заданное в форме"""
                flash(form.errors[error][0])
    if request.method == 'GET':
        form.validate_on_submit()

    return render_template('register.html', form=form)


@bp.route('/authenticated_user')
def authenticated_user():
    if current_user.is_authenticated:
        return jsonify(UserSchema().dump(current_user).data)

    abort(401)

