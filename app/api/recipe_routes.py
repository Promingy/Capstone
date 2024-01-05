from flask import Blueprint, request, session
from ..models import Recipe, Category, db
from ..forms import RecipeForm
from flask_login import login_required

recipe = Blueprint('recipes', __name__)

@recipe.route('')
@login_required
def get_all_recipes():
    """
    Route that returns all of the recipes needed for the homepage
    """
    categorized_recipes = {}

    # Iterates over all categories
    for index, category in enumerate(Category.query.all()):
        recipes = Recipe.query.filter(Recipe.category_id == index + 1).all()

        # if there are no recipies in cureent category
        # continue to next iterations
        if not len(recipes):
            continue

        category = category.to_dict()['category']

        # If category has recipes,
        # set category as key and all recipes as a list for the value
        categorized_recipes[category] = \
        [recipe.to_dict() for recipe in recipes]

    return categorized_recipes


@recipe.route('', methods=['POST'])
@login_required
def create_new_recipe():
    """
    Route to handle the creation of new recipes
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        newRecipe = Recipe(
            owner_id = int(session['_user_id']),
            category_id = int(data["category_id"]),
            title = data["title"],
            description = data["description"],
            servings = int(data["servings"]),
            prep_time = int(data["prep_time"]),
            cook_time = int(data["cook_time"]),
            preview_image = data["preview_image"],
        )

        db.session.add(newRecipe)
        db.session.commit()

        return newRecipe.to_dict()

    return form.errors, 400


@recipe.route('/<int:recipeId>')
def get_single_recipe(recipeId):
    """
    Route that returns all of the infor for a specific recipe
    """

    recipe = Recipe.query.get(recipeId)

    return recipe.to_dict(rating=True, reviews=True)


@recipe.route('/<int:recipeId>', methods=['PUT'])
@login_required
def update_recipe(recipeId):

    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    recipe = Recipe.query.get(recipeId)
    if not recipe:
        return {"error": "Resource not found"}, 404

    if form.validate_on_submit():
        data = form.data

        recipe.category_id = data['category_id']
        recipe.title = data['title']
        recipe.description = data['description']
        recipe.servings = data['servings']
        recipe.prep_time = data['prep_time']
        recipe.cook_time = data['cook_time']
        recipe.preview_image = data['preview_image']

        db.session.commit()
        return recipe.to_dict()

    else:
        return form.errors



@recipe.route('/<int:recipeId>', methods=['DELETE'])
@login_required
def delete_recipe(recipeId):
    recipe = Recipe.query.get(recipeId)

    if recipe and recipe.owner_id == int(session['_user_id']):
        db.session.delete(recipe)
        db.session.commit()
        return {"message": "successful"}

    elif not recipe:
        return {"error": "resource not found"}, 404

    else:
        return {"error": "Unauthorized"}, 403
