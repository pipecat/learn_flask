from flask import Flask, request, session, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'hahahahaha'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

password = '123'

class User(flask_login.UserMixin, db.Model):
    __tablename__ = 'login_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    login_count = db.Column(db.Integer, default=0)
    last_login_ip = db.Column(db.String(128), default='unknown')

db.create_all()

@flask_login.user_logged_in.connect_via(app)
def _track_logins(sender, user, **extra):
    user.login_count += 1
    user.last_login_ip = request.remote_addr
    db.session.add(user)
    db.session.commit()

@login_manager.user_loader
def user_loader(id):
    user = User.query.filter_by(id=id).first()
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
<form action='login' method='POST'>
    <input type='text' name='name' id='name' placeholder='name'></input>
    <input type='password' name='pw' id='pw' placeholder='password'></input>
    <input type='submit' name='submit'></input>
</form>
'''

    name = request.form.get('name')
    if request.form.get('pw') == password:
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        flask_login.login_user(user)
        return redirect(url_for('protected'))
    
    return 'Bad login'    

@app.route('/protected')
@flask_login.login_required
def protected():
    user = flask_login.current_user
    return 'Login as: {}| Login_count: {}|IP: {}'.format(user.name, user.login_count, user.last_login_ip)



if __name__ == '__main__':
    app.run(debug=True)