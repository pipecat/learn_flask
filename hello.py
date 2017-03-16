from flask import Flask, redirect, url_for, render_template, flash, session
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

class NameForm(Form):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField("Submit")
    

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'hard to guess'

@app.route('/', methods = ['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed your name!!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('hello_index.html',
        form=form, name=session.get('name') )

if __name__ == '__main__':
    app.run(debug=True)