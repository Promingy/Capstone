from .db import db, environment, SCHEMA
from flask_login import UserMixin

class Category(db.Model, UserMixin):
    __tablename__ = 'categories'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "category": self.category
        }

        return dictionary
