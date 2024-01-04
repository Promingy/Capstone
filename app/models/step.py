from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Step(db.Model, UserMixin):
    __tablename__ = "steps"

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "recipe_id": self.recipe_id,
            "step_number": self.step_number,
            "description": self.description
        }

        return dictionary
