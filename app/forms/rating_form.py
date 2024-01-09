from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class RatingForm(FlaskForm):
    recipe_id = IntegerField('recipe_id', validators=[DataRequired()])
    user_id = IntegerField('user_id', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    submit = SubmitField('submit')
