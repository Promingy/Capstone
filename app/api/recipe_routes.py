from flask import Blueprint
from ..models import Recipe, Category

recipe = Blueprint('recipes', __name__)

@recipe.route('/')
def get_all_recipes():
    """
    Route that returns all of the recipes needed for the homepage
    """
    categorized_recipes = {}

    for index, category in enumerate(Category.query.all()):
        recipes = Recipe.query.filter(Recipe.category_id == index + 1).all()

        if not len(recipes):
            continue

        category = category.to_dict()['category']

        categorized_recipes[category] = \
        [recipe.to_dict() for recipe in recipes]

    return categorized_recipes
    return all_recipes

@recipe.route('/<int:recipeId>')
def get_single_recipe(recipeId):
    """
    Route that returns all of the infor for a specific recipe
    """

    recipe = Recipe.query.get(recipeId)

    return recipe.to_dict(rating=True, reviews=True)
