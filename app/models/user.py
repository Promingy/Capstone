from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    recipes = db.relationship('Recipe', back_populates='owner')
    reviews = db.relationship('Review', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        dictionary = {
            'id': self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "bio": self.bio,
            'email': self.email,
            'profile_pic': self.profile_pic
        }

        return dictionary
