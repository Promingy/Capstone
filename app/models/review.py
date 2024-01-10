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
    # rating = db.Column(db.Integer, default=5)
    private = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())

    recipe = db.relationship('Recipe', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')

    def to_dict(self, name=False):
        dictionary = {
            "id": self.id,
            'user_id': self.user_id,
            "recipe_id": self.recipe_id,
            "body": self.body,
            "edited": self.edited,
            "private": self.private,
            # "rating": self.rating,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

        if name:
            review_owner = self.user.to_dict()
            dictionary['name'] = f"{review_owner['first_name'].title()} {review_owner['last_name'].title()}"


        return dictionary
