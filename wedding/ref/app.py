# coding=utf-8
"""App module.

This module contains factory methods for the set up of the the app. All flask
blueprints should be imported and attached to the app here.

"""

from flask import Flask
from resting.api import api_bp
from resting.database import db
from resting.config import TestingConfig, DevelopmentConfig, ProductionConfig


def create_app(config: str) -> Flask:
    """Flask app factory with support for multiple preset configurations.
    Create an app using one of three possible configuration settings -
    'testing', 'development', 'production'. For more information on the
    configuration settings, refer to config.py
    Args:
        config: Config string- 'testing', 'development' or 'production'.
    Returns:
        Flask app instance with the specified configuration
    """
    app = Flask(__name__)

    configs = {
        'testing': TestingConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }

    app.config.from_object(configs[config])

    app.register_blueprint(api_bp)

    db.init_app(app)

    return app


# noinspection PyUnresolvedReferences
def init_db(reset: bool) -> None:
    """Database initialisation script to create (and optionally drop) tables.
    Args:
        reset: If True, drop and recreate all tables.
    """
    # import all models here
    import resting.models  # flake8: noqa  # pylint: disable=unused-variable

    if reset:
        db.drop_all()
    db.create_all()
