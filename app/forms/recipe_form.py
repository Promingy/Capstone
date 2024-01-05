from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    category_id = IntegerField('category_id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    servings = IntegerField('servings', validators=[DataRequired()])
    prep_time = IntegerField('prep_time', validators=[DataRequired()])
    cook_time = IntegerField('cook_time', validators=[DataRequired()])
    preview_image = StringField('preview_image', validators=[DataRequired()])
    submit = SubmitField('submit')
