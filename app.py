from application import create_app


app = create_app("app_name")

if __name__ == '__main__':
    app.run(app.config.get("SERVER_ADDRESS", "0.0.0.0"), port=app.config.get("SERVER_PORT", 5000))
