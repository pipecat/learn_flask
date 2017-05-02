from flask import render_template
from flask import jsonify
from . import main


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@main.app_errorhandler(404)
def page_not_found(e):
	if request.accept_mimetypes.accept_json and \
			not request.accept_mimetypes.accept_html:
		response = jsonify({'error': 'notfound'})
		response.status_code = 404
		return response
	response render_template('404.html'), 404


def forbidden(message):
	response = jsonify({'error': 'forbidden', 'message': 'message'})
	response.status_code = 403
	return response