from datetime import datetime
from flask import render_template, session, redirect, url_for, abort
from flask.ext.login import login_required

from . import main
#from .forms import NameForm
from .. import db
from ..models import User, Permission
from ..decorators import permission_required, admin_required

@main.route('/', methods=['POST', 'GET'])
def index():
    '''form = NameForm
    if form.validate_on_submit():
        # ...

        return redirect(url_for('index'))
    return render_template('index.html',
                            form=form, name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())
    ''' 
    return render_template('index.html')

@main.route('/testadmin')
@login_required
@admin_required
def for_admin_only():
    return "For only administrators!"

@main.route('/testmoderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For only moderators!"

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500