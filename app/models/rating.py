from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Rating(db.Model, UserMixin):
    __tablename__ = 'ratings'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")))
    rating = db.Column(db.Integer)

    user = db.relationship('User', back_populates='ratings')
    recipe = db.relationship('Recipe', back_populates='ratings')

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "rating": self.rating
        }

        return dictionary
