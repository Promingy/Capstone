from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MeasurementForm(FlaskForm):
    measurement_name = StringField('measurement_name', validators=[DataRequired()])
