from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

class StepForm(FlaskForm):
    step_number = FloatField('step_number', validators=[DataRequired()])
    step_description = StringField('step_description', validators=[DataRequired()])
