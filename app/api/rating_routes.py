from flask import Blueprint, request, session
from ..models import Rating, db, Like
from ..forms import RatingForm
from flask_login import login_required

rating = Blueprint('ratings', __name__)

@rating.route('/<int:ratingId>', methods=['PUT'])
@login_required
def update_rating(ratingId):

    form = RatingForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    rating = Rating.query.get(ratingId)

    if not rating:
        return {"errors": "Rating not found"}, 404

    if form.validate_on_submit():
        data = form.data

        rating.rating = data['rating']

        db.session.commit()

        return rating.to_dict()

    else:
        return {"errors": form.errors}, 400

@rating.route('/<int:ratingId>', methods=['DELETE'])
@login_required
def delete_rating(ratingId):

    rating = Rating.query.get(ratingId)

    if not rating:
        return {"errors": "Rating not found"}, 404

    if int(rating.to_dict()['user_id']) == int(session['_user_id']):
        db.session.delete(rating)
        db.session.commit()

        return {"message": "successfully deleted"}

    else:
        return {"errors": "Unauthorized"}, 401
