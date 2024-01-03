from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
