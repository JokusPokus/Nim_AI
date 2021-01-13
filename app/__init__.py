from flask import Flask
from flask_session import Session
from config import config


session = Session()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize Plugins
    session.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    # Routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.add_url_rule('/', endpoint='index')

    from .AI import ai as ai_blueprint
    app.register_blueprint(ai_blueprint)