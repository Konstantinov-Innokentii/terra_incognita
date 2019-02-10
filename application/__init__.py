from flask import Flask


def create_app(name):

    import os

    APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
    STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')

    app = Flask(name, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
    app.config.from_object("config")

    with app.app_context():
        from .modules import db
        db.init_app(app)

        from .modules.bcrypt import bcrypt
        bcrypt.init_app(app)
        from .landing import blueprint as land_bp
        app.register_blueprint(land_bp)

        from .auth import blueprint as auth_bp
        app.register_blueprint(auth_bp)

    return app
