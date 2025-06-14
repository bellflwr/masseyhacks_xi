from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from . import blueprints

    app.register_blueprint(blueprints.home, url_prefix="/")
    app.register_blueprint(blueprints.posters, url_prefix="/posters")
    app.register_blueprint(blueprints.selector, url_prefix="/selector")

    return app
