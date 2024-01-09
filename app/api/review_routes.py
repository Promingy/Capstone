from flask import Blueprint, session, request
from ..models import Review, Like
from ..forms import ReviewForm
from flask_login import login_required

review = Blueprint('reviews', __name__)

@review.route('')
def get_single_recipe_reviews():
    pass
