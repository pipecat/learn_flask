from flask import render_template
from . import auth

@auth.route('/')
def login():
    return render_template('auth_login.html')