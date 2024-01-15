from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

class QuantityForm(FlaskForm):
    ingredient = StringField('ingredient', validators=[DataRequired()])
    ingredient_quantity = FloatField('ingredient_quantity', validators=[DataRequired()])
    measurement_id = IntegerField('measurement_id', validators=[DataRequired()])
