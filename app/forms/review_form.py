from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    edited = BooleanField('edited')
    private = BooleanField('private')
    submit = SubmitField('submit')
