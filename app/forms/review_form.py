from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    submit = SubmitField('submit')
