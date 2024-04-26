from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Recipe

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:userId>/recipes')
def get_user_routes(userId):
    """
    Query for all recipes from a specific user
    """
    recipes = Recipe.query.filter(Recipe.owner_id == userId).all()
    owner = User.query.get(userId)

    return {"owner": owner.to_dict(), "recipes":{recipe.to_dict()['id']: recipe.to_dict(rating=True) for recipe in recipes}}

@user_routes.route('/<int:userId>/saved-recipes')
def get_user_saved_recipes(userId):
    """
    Query for all saved recipes from a specific user
    """

    user = User.query.get(userId)
    saved_recipes = user.saved_recipes

    return {
            # "user": user.to_dict(),
            "saved_recipes": {saved_recipe.to_dict()['id']: saved_recipe.to_dict(rating=True) for saved_recipe in saved_recipes}
        }

@user_routes.route('/<int:userId>/recently-viewed')
def get_user_recently_viewed(userId):
    """
    Query for all recently viewed recipes from a specific user
    """

    user = User.query.get(userId)
    viewed_recipes = user.viewed_recipes
    viewed_recipes = viewed_recipes[::-1]


    return {
        # "viewed_recipes": {viewed_recipe.to_dict()['id']: viewed_recipe.to_dict(rating=True) for viewed_recipe in viewed_recipes}
        "viewed_recipes": [viewed_recipe.to_dict(rating=True) for viewed_recipe in viewed_recipes]
    }
