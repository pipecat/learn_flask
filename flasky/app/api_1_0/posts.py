from flask import jsonify
from . import api
from .authentication import auth
from ..models import Post


@api.route('/posts/')
@auth.login_required
def get_posts():
	posts = Post.query.all()
	return jsonify({ 'posts': [post.to_json() for post in posts] })

@api.route('/posts/<int:id>')
@auth.login_required
def get_post():
	post = Post.query.get_or_404(id)
	return jsonify(post.to_json())