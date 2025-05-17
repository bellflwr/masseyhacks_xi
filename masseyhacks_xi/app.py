from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from . import blueprints

    return app
