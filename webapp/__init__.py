from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = "dev"

    return app
