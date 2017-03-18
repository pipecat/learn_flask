from flask import Flask, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('learn_flask_bootstrap.html')

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

if __name__ == '__main__':
    app.run(debug=True)