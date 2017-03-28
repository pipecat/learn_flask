from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

def create_app():
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app