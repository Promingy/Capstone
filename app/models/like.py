from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

Like = db.Table(
    "likes",
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('review_id', db.Integer, db.ForeignKey(add_prefix_for_prod('reviews.id')), primary_key=True)
)

if environment == 'production':
    Like.schema = SCHEMA
