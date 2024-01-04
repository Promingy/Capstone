from .db import db, environment, SCHEMA
from flask_login import UserMixin

class Measurement(db.Model, UserMixin):
    __tablename__ = 'measurements'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    measurement_name = db.Column(db.String)

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "measurement_name": self.measurement_name
        }

        return dictionary
