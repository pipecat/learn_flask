from flask import Flask,request,abort,redirect,url_for,make_response,render_template

app = Flask(__name__)
app.config.from_object('redirect_config')

@app.route('/people/')
def people():
    name =request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name:{}; UA: {}'.format(name,user_agent)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User: {} longin.'.format(user_id)
    else:
        return 'Open Login page'


@app.route('/secret/')
def secret():
    abort(401)
    print 'This is never executed'


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'),404)
    return resp

if __name__ == '__main__':
    app.run(port=9000,debug=app.debug)
