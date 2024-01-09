from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Quantity(db.Model, UserMixin):
    __tablename__ = 'quantities'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')))
    ingredient_measurement_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('measurements.id')))
    ingredient = db.Column(db.String, nullable=False)
    ingredient_quantity = db.Column(db.Integer, nullable=False)

    recipe = db.relationship('Recipe', back_populates='quantities')

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "recipe_id": self.recipe_id,
            "ingredient_measurement_id": self.ingredient_measurement_id,
            "ingredient": self.ingredient,
            "ingredient_quantity": self.ingredient_quantity
        }

        return dictionary
