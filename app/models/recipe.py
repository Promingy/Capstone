from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Recipe(db.Model, UserMixin):
    __tablename__ = 'recipes'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("categories.id")), nullable=False)
    title = db.Column(db.String(75), nullable=False)
    description = db.Column(db.String, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    preview_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    reviews = db.relationship('Review', back_populates='recipe')

    def to_dict(self, rating=False, reviews=False):
        dictionary = {
            "id": self.id,
            "owner_id": self.owner_id,
            "category_id": self.category_id,
            "title": self.title,
            "description": self.description,
            "servings": self.servings,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "preview_image": self.preview_image,
            "created_at": self.created_at
        }

        if rating:
            avg_rating = sum([review.to_dict()['rating'] for review in self.reviews]) / len(self.reviews)
            dictionary['avg_rating'] = avg_rating

        if reviews:
            dictionary['reviews'] = sorted([review.to_dict() for review in self.reviews], key=lambda msg: datetime(msg['created_at'].year, msg['created_at'].month, msg['created_at'].day, msg['created_at'].hour, msg['created_at'].minute, msg['created_at'].second), reverse=True)
        return dictionary
