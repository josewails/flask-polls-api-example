from flask import Flask

from .questions.views import questions
from .answers.views import answers
from .core.views import core
from .users.views import users
from .exts import db, ma, migrate, swagger


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    swagger.init_app(app)


def register_blueprints(app):
    app.register_blueprint(core)
    app.register_blueprint(users)
    app.register_blueprint(questions)
    app.register_blueprint(answers)


def create_app(config):
    # Define WSGI application object
    app = Flask(__name__)

    # Configurations
    app.config.from_object(config)

    # register extensions

    register_extensions(app)

    # register blueprints
    register_blueprints(app)

    return app


app = create_app('config')
