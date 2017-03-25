from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from config import config

bootstrap = Boorstrap()
db = SQLAlchemy()
mail = Mail()
moment = moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap = Boorstrap(app)
    db = SQLAlchemy(app)
    mail = Mail(app)
    moment = moment(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app