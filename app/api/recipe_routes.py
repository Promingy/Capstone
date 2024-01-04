from flask import Blueprint
from ..models import Recipe, Category

recipe = Blueprint('recipes', __name__)

@recipe.route('/')
def get_all_recipes():
    """
    Route that returns all of the recipes needed for the homepage
    """
    all_recipes = [recipe.to_dict(rating=True) for recipe in Recipe.query.all()]
    return all_recipes
    # categories = [f"{category.to_dict()['id']}  {category.to_dict()['category']}" for category in Category.query.all()]

    # category1_recipes = [recipe.to_dict() for recipe in Recipe.query.filter(Recipe.category_id == 1).all()]
    # category2_recipes = [recipe.to_dict() for recipe in Recipe.query.filter(Recipe.category_id == 2).all()]

    # categorized_recipes = {
    #     "categories": categories,
    #     "Appetizer": category1_recipes,
    #     "Main Course": category2_recipes
    # }
    # return categorized_recipes

@recipe.route('/<int:recipeId>')
def get_single_recipe(recipeId):
    """
    Route that returns all of the infor for a specific recipe
    """

    recipe = Recipe.query.get(recipeId)

    return recipe.to_dict(rating=True, reviews=True)
