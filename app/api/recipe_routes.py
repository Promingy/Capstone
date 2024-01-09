from flask import Blueprint, request, session
from ..models import Recipe, Category, db, Quantity, Step
from ..forms import RecipeForm, QuantityForm, StepForm, ReviewForm
from flask_login import login_required
from app.aws import (upload_file_to_s3, get_unique_filename)

recipe = Blueprint('recipes', __name__)

@recipe.route('')
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

        # category = category.to_dict()['category']
        category = category.to_dict()['id']

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
    ingredients = request.get_json()['ingredients']
    steps = request.get_json()['steps']

    form = RecipeForm()
    form2 = QuantityForm()
    form3 = StepForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    form2['csrf_token'].data = request.cookies['csrf_token']
    form3['csrf_token'].data = request.cookies['csrf_token']

    # Validate each ingredient in the recipe - all should pass
    for key in ingredients:
        ingredient = ingredients[key]

        form2.ingredient.data = ingredient['ingredient']
        form2.ingredient_quantity.data = ingredient['ingredient_quantity']
        form2.measurement_id.data = ingredient['ingredient_measurement_id']

        if not form2.validate_on_submit():
            break

    # validate each step in the recipe - all should pass
    for key in steps:
        step = steps[key]

        form3.step_number.data = step['step_number']
        form3.step_description.data = step['description']

        if not form3.validate_on_submit():
            break

    # run validate_on_submit on all forms to catch errors for all forms
    form.validate_on_submit()
    form2.validate_on_submit()
    form3.validate_on_submit()

    # if form passes validations, add to database
    if form.validate_on_submit() and form2.validate_on_submit() and form3.validate_on_submit():
        data = form.data

        # create and add new recipe to the db
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

        # Create and add new quantity for every ingredient to the db now that the recipe exists
        for key in ingredients:
            ingredient = ingredients[key]

            newQuantity = Quantity(
                recipe_id = newRecipe.to_dict()['id'],
                ingredient_measurement_id = ingredient['ingredient_measurement_id'],
                ingredient = ingredient['ingredient'],
                ingredient_quantity = ingredient['ingredient_quantity']
            )

            db.session.add(newQuantity)

        # Create new step in the db for each step
        for key in steps:
            step = steps[key]

            newStep = Step(
                recipe_id = newRecipe.to_dict()['id'],
                step_number = step['step_number'],
                description = step['description']
            )

            db.session.add(newStep)

        db.session.commit()

        return newRecipe.to_dict()

    else:
        errors = {}

        # add every error from all forms into a single error dictionary to return
        for field, error in form.errors.items():
            errors[field] = error

        for field, error in form2.errors.items():
            errors[field] = error

        for field, error in form3.errors.items():
            errors[field] = error

        return {"errors": errors}, 400

@recipe.route('/<int:recipeId>')
def get_single_recipe(recipeId):
    """
    Route that returns all of the info for a specific recipe
    """

    recipe = Recipe.query.get(recipeId)
    recipe = recipe.to_dict(rating=True, reviews=True, steps=True, quantities=True)

    return recipe

@recipe.route('/<int:recipeId>', methods=['PUT'])
@login_required
def update_recipe(recipeId):

    ingredients = request.get_json()['ingredients']
    steps = request.get_json()['steps']

    form = RecipeForm()
    form2 = QuantityForm()
    form3 = StepForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    form2['csrf_token'].data = request.cookies['csrf_token']
    form3['csrf_token'].data = request.cookies['csrf_token']

    recipe = Recipe.query.get(recipeId)

    if not recipe:
        return {"error": "Resource not found"}, 404

    # verify all ingredients before updating recipe
    for key in ingredients:
        ingredient = ingredients[key]

        form2.ingredient.data = ingredient['ingredient']
        form2.ingredient_quantity.data = ingredient['ingredient_quantity']
        form2.measurement_id.data = ingredient['ingredient_measurement_id']

        if not form2.validate_on_submit():
            break

    # verify all steps before updating recipe
    for key in steps:
        step = steps[key]

        form3.step_number.data = step['step_number']
        form3.step_description.data = step['description']

        if not form3.validate_on_submit():
            break

    # run validate on submit for all forms so that we cat errors for all the forms at once
    form.validate_on_submit()
    form2.validate_on_submit()
    form3.validate_on_submit()

    # if all forms pass the validation, run the update logic
    if form.validate_on_submit() and form2.validate_on_submit() and form3.validate_on_submit():
        data = form.data
        db_ingredients = Quantity.query.filter(Quantity.recipe_id == recipeId).all()
        db_steps = Step.query.filter(Step.recipe_id == recipeId).all()

        recipe.category_id = data['category_id']
        recipe.title = data['title']
        recipe.description = data['description']
        recipe.servings = data['servings']
        recipe.prep_time = data['prep_time']
        recipe.cook_time = data['cook_time']
        recipe.preview_image = data['preview_image']

        # check if the user given ingredients list is longer than what's in our database
        # if so, add the ingredient to the database
        # it already passed the validation check if we're right here
        #/ if statement removed - was preventing new ingredients being added if some were removed
        #/ ex. 1 ingredient removed, 1 ingredient added - length would be the same.
        # if len(db_ingredients) < len(ingredients):
        for ingredient in ingredients:
            reqIngredient = ingredients[ingredient]
            try:
                reqIngredient['id']
            except:
                newIngredient = Quantity(
                    recipe_id = recipeId,
                    ingredient_measurement_id = reqIngredient['ingredient_measurement_id'],
                    ingredient = reqIngredient['ingredient'],
                    ingredient_quantity = reqIngredient['ingredient_quantity']
                )
                db.session.add(newIngredient)
                db.session.commit()
                print(ingredients[ingredient], ingredients)
                ingredients[ingredient]['id'] = newIngredient.to_dict()['id']
        # if a new ingredients list is less than what the db has, remove the ingredients
        if len(db_ingredients) > len(ingredients):
            for ingredient in db_ingredients:
                try:
                    ingredients[str(ingredient.to_dict()['id'])]
                except:
                    db.session.delete(ingredient)

        for key in ingredients:
            new_ingredient = ingredients[key]
            db_ingredient = Quantity.query.get(new_ingredient['id'])

            db_ingredient.ingredient = new_ingredient['ingredient']
            db_ingredient.ingredient_quantity = new_ingredient['ingredient_quantity']
            db_ingredient.measurement_id = new_ingredient['ingredient_measurement_id']

        # if the user give steps is greater than the db steps, add new steps to the database
        #/ if statement removed for the same reason as above
        # if len(db_steps) < len(steps):
        for step in steps:
            reqStep = steps[step]
            try:
                reqStep['id']
            except:
                newStep = Step(
                    recipe_id = recipeId,
                    step_number = reqStep['step_number'],
                    description = reqStep['description']
                )
                db.session.add(newStep)
                db.session.commit()
                steps[step]['id'] = newStep.to_dict()['id']
        # else if, user give steps is less than the database, remove steps from the db
        if len(db_steps) > len(steps):
            for step in db_steps:
                try:
                    steps[str(step.to_dict()['step_number'])]
                except:
                    db.session.delete(step)

        for key in steps:
            new_step = steps[key]
            db_step = Step.query.get(new_step['id'])

            db_step.step_number = new_step['step_number']
            db_step.description = new_step['description']


        db.session.commit()
        return recipe.to_dict()

    else:
        errors = {}

        # add errors from all forms to a dictionary and return the dictionary
        for field, error in form.errors.items():
            errors[field] = error

        for field, error in form2.errors.items():
            errors[field] = error

        for field, error in form3.errors.items():
            errors[field] = error

        return {"errors": errors}, 400

@recipe.route('/<int:recipeId>', methods=['DELETE'])
@login_required
def delete_recipe(recipeId):
    recipe = Recipe.query.get(recipeId)
    quantities = Quantity.query.filter(Quantity.recipe_id == recipeId).all()
    steps = Step.query.filter(Step.recipe_id == recipeId).all()

    if recipe and recipe.owner_id == int(session['_user_id']):
        db.session.delete(recipe)
        [db.session.delete(quantity) for quantity in quantities]
        [db.session.delete(step) for step in steps]

        db.session.commit()
        return {"message": "successful"}

    elif not recipe:
        return {"error": "resource not found"}, 404

    else:
        return {"error": "Unauthorized"}, 403

@recipe.route('/<int:recipeId>/reviews', methods=['POST'])
@login_required
def post_review(recipeId):

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print('~~~~~~~~~~~~~', form.data)


    if form.validate_on_submit():
        data = form.data
