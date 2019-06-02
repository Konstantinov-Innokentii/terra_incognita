from flask import Flask


def create_app(name):

    import os
    from contextlib import suppress
    from importlib import import_module

    APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
    STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')

    app = Flask(name, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
    app.config.from_object("config")

    with app.app_context():

        from .modules.db import session_factory
        session_factory.init_app(app)

        from .modules.bcrypt import bcrypt
        bcrypt.init_app(app)

        from .modules.login import login_manager
        login_manager.init_app(app)

        apps = {
            "application.react": None,
            "application.api.v1": "/api/v1",
            "application.auth": "/auth",
            "application.terra": "/terra",
            "application.landing": None,
        }

        load_apps = True
        if load_apps:
            for app_ in apps.keys():
                import_module(app_)

            for module in [".models", ".views", ".api"]:
                for app_ in apps.keys():
                    try:
                        import_module(module, app_)
                    except Exception as e:
                        if not str(e).startswith("No module named"):
                            raise

            for app_, url in apps.items():
                with suppress(ImportError):
                    bp = getattr(import_module(".blueprint", app_), "blueprint")
                    app.register_blueprint(bp, url_prefix=url)

    return app
