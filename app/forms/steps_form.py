from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class StepForm(FlaskForm):
    step_number = IntegerField('step_number', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
