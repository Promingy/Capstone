from flask import Blueprint
from flask_login import login_required
from app.models import User, Recipe, db
from app.models.viewed_recipe import ViewedRecipe

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
    viewed_recipes = [recipe.to_dict() for recipe in user.viewed_recipes]

    # add viewed_at key to each recipe in viewed_recipes
    for recipe in viewed_recipes:
        view_date = db.session.query(ViewedRecipe).filter(ViewedRecipe.c.user_id == userId, ViewedRecipe.c.recipe_id == int(recipe['id'])).first()
        recipe['viewed_at'] = view_date[2]

    # sort viewed_recipes by viewed_at
    viewed_recipes = sorted(viewed_recipes, key=lambda x: x['viewed_at'], reverse=True)

    return {
        "viewed_recipes": viewed_recipes
    }

@user_routes.route('/<int:userId>/cooked-recipes')
def get_user_cooked_recipes(userId):
    """
    Query for all cooked recipes from a specific user
    """

    user = User.query.get(userId)
    cooked_recipes = user.cooked_recipes

    return {
        "cooked_recipes": {cooked_recipe.to_dict()['id']: cooked_recipe.to_dict(rating=True) for cooked_recipe in cooked_recipes}
    }
