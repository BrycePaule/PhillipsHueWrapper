from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from CustomObjects.LightGroup import LightGroup
from CustomObjects.Light import Light

class LightToggleForm(FlaskForm):
    selection = SelectField('Select a light to turn off', coerce=Light, validate_choice=False)
    submit = SubmitField('Submit')

