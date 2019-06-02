# -*- coding: utf_8 -*-

from flask_wtf import FlaskForm
from flask_sqlalchemy_session import current_session
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from ..models.user import User


class Unique(object):
    def __init__(self, model, field, message=u'This element already exists.'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = current_session.query(self.model).filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Username is required')])
    password = PasswordField('Password', validators=[DataRequired('Password is required')])


class RegistrationFormBase(FlaskForm):
    username = StringField('Username', [
        DataRequired()
    ])

    email = StringField('Email Address', [
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', [
        DataRequired(message='Password is required'),
        Length(min=6, max=25)
    ])

    confirm = PasswordField('Repeat Password', [
        EqualTo('password', 'Passwords must match')
    ])


class RegistrationForm(RegistrationFormBase):
    username = StringField('Username', [
        DataRequired('Username is required'),
        Unique(User, User.username)
    ])

    email = StringField('Email Address', [
        DataRequired('Email is required'),
        Email(),
        Unique(User, User.email)
    ])
