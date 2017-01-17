from flask import Flask
from flask.ext.script import Manager
import tutorial_setting
app = Flask(__name__)
app.config.from_object(tutorial_setting)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1> Hello World by flask!! </h1>'

@app.route('/user/<user_name>/')
def username(user_name):
    return 'Hello %s' % user_name


if __name__ == '__main__':
    manager.run()
