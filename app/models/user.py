from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .like import Like
from .saved_recipe import SavedRecipe
from .viewed_recipe import ViewedRecipe

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    recipes = db.relationship('Recipe', back_populates='owner')
    reviews = db.relationship('Review', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    user_likes = db.relationship('Review', secondary=Like, back_populates='review_likes')
    saved_recipes = db.relationship('Recipe', secondary=SavedRecipe, back_populates='saved_users')
    viewed_recipes = db.relationship('Recipe', secondary=ViewedRecipe, back_populates='users_viewed_recipe')

    @property
    def password(self):
        return self.hashed_password

    # @password.setter
    # def password(self, password):
    #     self.hashed_password = generate_password_hash(password)

    @password.setter
    def password(self, password):
        # New code starts here #################
        if password == 'OAUTH':
            self.hashed_password = 'OAUTH' # If we look at the password_checker() method, we see that it hashes the user input and compares it
                        ## during login. With this adjustment, even a data breach would NOT expose our Oauth users to
                        ### having their accounts accessed with our default password for Oauth logins, 'OAUTH', as it would never
                        #### hash to that value.
            return
        # New code ends here ####################
        else:
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
