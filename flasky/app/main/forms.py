from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField, SubmitField
from wtforms.validators import Required, Length, Email
from wtforms import ValidationError

class EditProfileForm(Form):
    """docstring for EditProfileForm"""
    name = StringField(' Real name ', validators=[Length(0,64)])
    location = StringField('Location', validators=[Length(0,64)])
    about_me = TextField('About me')
    submit = SubmitField('Submit')
