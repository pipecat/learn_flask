from flask import Flask, request, jsonify

from ext import db
from users import User

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/users', methods=['POST'])
def users():
    username = request.get('name')

    user = User(username)
    print 'User ID: {}'.format(user.id)
    db.session.add(user)
    sb.session.commit()

    return jsonify({'id': user.id})

if __name__ == '__main__':
    app.run()