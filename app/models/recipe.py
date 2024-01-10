from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask import session
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
    description = db.Column(db.String(2000), nullable=False)
    servings = db.Column(db.Float, nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    preview_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    reviews = db.relationship('Review', back_populates='recipe')
    owner = db.relationship('User', back_populates=('recipes'))
    quantities = db.relationship('Quantity', back_populates='recipe')
    steps = db.relationship('Step', back_populates='recipe')
    ratings = db.relationship('Rating', back_populates='recipe')

    def to_dict(self, rating=False, reviews=False, steps=False, quantities=False, user_rating=False):
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
            "created_at": self.created_at,
            "owner": self.owner.to_dict()
        }

        if steps:
            dictionary['steps'] = {}

            for step in self.steps:
                dictionary['steps'][step.to_dict()['step_number']] = step.to_dict()

        if quantities:
            dictionary['ingredients'] = {}

            for quantity in self.quantities:
                dictionary['ingredients'][quantity.to_dict()['id']] = quantity.to_dict()

        if rating:
            # calculates the average rating for the current recipe and adds it to the dictionary
            avg_rating = 0

            if len(self.ratings):
                avg_rating = sum(rating.to_dict()['rating'] for rating in self.ratings) / len(self.ratings)


            dictionary['avg_rating'] = avg_rating

            # adds total amount of reviews for the current refcipe to the dictionary
            dictionary['all_ratings'] = len(self.ratings)
            dictionary['ratings'] = [rating.to_dict() for rating in self.ratings]

        if reviews:
            # Adds list of reviews, sorted by date, to the dictionary
            dictionary['reviews'] = sorted([review.to_dict(name=True) for review in self.reviews],
                                           key=lambda msg: datetime(msg['created_at'].year,
                                                                    msg['created_at'].month,
                                                                    msg['created_at'].day,
                                                                    msg['created_at'].hour,
                                                                    msg['created_at'].minute,
                                                                    msg['created_at'].second),
                                                                    reverse=True)

        if user_rating:
            for rating in self.ratings:
                if rating.to_dict()['user_id'] == int(session['_user_id']):
                    dictionary["user_rating"] = rating.to_dict()

        return dictionary
