from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class QuantityForm(FlaskForm):
    ingredient = StringField('ingredient', validators=[DataRequired()])
    ingredient_quantity = IntegerField('ingredient_quantity', validators=[DataRequired()])
