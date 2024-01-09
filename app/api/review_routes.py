from flask import Blueprint, session, request
from ..models import Review, Like, db
from ..forms import ReviewForm
from flask_login import login_required

review = Blueprint('reviews', __name__)

@review.route('/<int:reviewId>', methods=['DELETE'])
@login_required
def delete_review(reviewId):

    review = Review.query.get(reviewId)

    if not review:
        return {"errors": "review not found"}, 404

    if int(review.to_dict()['user_id']) == int(session['_user_id']):
        db.session.delete(review)
        db.session.commit()

        return {"message": "success"}
