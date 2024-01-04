from .db import environment, add_prefix_for_prod, SCHEMA, db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Review(db.Model, UserMixin):
    __tablename__ = 'reviews'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')))
    body = db.Column(db.String)
    edited = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer, default=5)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())

    recipe = db.relationship('Recipe', back_populates='reviews')

    def to_dict(self):
        dictionary = {
            "id": self.id,
            'user_id': self.user_id,
            "recipe_id": self.recipe_id,
            "body": self.body,
            "edited": self.edited,
            "rating": self.rating,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

        return dictionary
