from flask import Blueprint, request, session
from ..models import Recipe, Category, db, Quantity, Step, Rating, Review, User
from ..forms import RecipeForm, QuantityForm, StepForm, ReviewForm, RatingForm
from flask_login import login_required, current_user

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
        [recipe.to_dict(rating=True) for recipe in recipes]

    return categorized_recipes

@recipe.route('', methods=['POST'])
@login_required
def create_new_recipe():
    """
    Route to handle the creation of new recipes
    """
    ingredients = {}
    steps = {}

    try:
        ingredients = request.get_json()['ingredients']
    except:
        ingredients = {}
    try:
        steps = request.get_json()['steps']
    except:
        steps = {}

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
    recipe = recipe.to_dict(rating=True,
                            reviews=True,
                            steps=True,
                            quantities=True,
                            user_rating=current_user.is_authenticated)

    # add recipe to users recently viewed recipes
    if (current_user.is_authenticated):
        user = User.query.get(int(session['_user_id']))
        updatedRecipe = Recipe.query.get(recipeId)

        user.viewed_recipes.append(updatedRecipe)
        db.session.commit()

    return recipe

@recipe.route('/<int:recipeId>', methods=['PUT'])
@login_required
def update_recipe(recipeId):

    ingredients = request.get_json()['ingredients']
    steps = request.get_json()['steps']
    delIngredients = request.get_json()['ingredientsToDelete']
    delSteps = request.get_json()['stepsToDelete']

    form = RecipeForm()
    form2 = QuantityForm()
    form3 = StepForm()

    form['csrf_token'].data = \
    form2['csrf_token'].data = \
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

        recipe.category_id = data['category_id']
        recipe.title = data['title']
        recipe.description = data['description']
        recipe.servings = data['servings']
        recipe.prep_time = data['prep_time']
        recipe.cook_time = data['cook_time']
        recipe.preview_image = data['preview_image']

        # iterate over ingredients and check if they have an id
        # if they do, update the ingredient in the database
        # if they don't, create a new ingredient in the database
        for ingredient in ingredients:
            reqIngredient = ingredients[ingredient]
            try:
                reqIngredient['id']

                db_ingredient = Quantity.query.get(reqIngredient['id'])

                db_ingredient.ingredient = reqIngredient['ingredient']
                db_ingredient.ingredient_quantity = reqIngredient['ingredient_quantity']
                db_ingredient.ingredient_measurement_id = reqIngredient['ingredient_measurement_id']
            except:
                newIngredient = Quantity(
                    recipe_id = recipeId,
                    ingredient_measurement_id = reqIngredient['ingredient_measurement_id'],
                    ingredient = reqIngredient['ingredient'],
                    ingredient_quantity = reqIngredient['ingredient_quantity']
                )
                db.session.add(newIngredient)
                db.session.commit()
                ingredients[ingredient]['id'] = newIngredient.to_dict()['id']

        # Iterate over the ingredientsToDelete object and delete them from the database
        for ingredient in delIngredients:
            ingredient = delIngredients[ingredient]
            delIngredient = Quantity.query.get(ingredient['id'])
            db.session.delete(delIngredient)

        # iterate over steps and check if they have an id
        # if they do, update the step in the database
        # if they don't, create a new step in the database
        for step in steps:
            reqStep = steps[step]
            try:
                reqStep['id']
                db_step = Step.query.get(reqStep['id'])

                db_step.step_number = reqStep['step_number']
                db_step.description = reqStep['description']
            except:
                newStep = Step(
                    recipe_id = recipeId,
                    step_number = reqStep['step_number'],
                    description = reqStep['description']
                )
                db.session.add(newStep)
                db.session.commit()
                steps[step]['id'] = newStep.to_dict()['id']

        # Iterate over steps that are in delsteps and delete them from the database
        for step in delSteps:
            step = delSteps[step]
            delStep = Step.query.get(step['id'])
            db.session.delete(delStep)

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


    if not recipe:
        return {"error": "resource not found"}, 404

    if recipe and recipe.owner_id == int(session['_user_id']):
        db.session.delete(recipe)
        [db.session.delete(quantity) for quantity in quantities]
        [db.session.delete(step) for step in steps]

        db.session.commit()
        return {"message": "successful"}

    else:
        return {"error": "Unauthorized"}, 403

@recipe.route('/<int:recipeId>/reviews', methods=['POST'])
@login_required
def post_review(recipeId):
    """
    Route that validates given data and creates a new post
    """

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        newReview = Review(
            user_id = int(session['_user_id']),
            recipe_id = int(recipeId),
            body = data['body'],
            edited = data['edited'],
            private = data['private'],
        )

        db.session.add(newReview)
        db.session.commit()

        return newReview.to_dict()

    else:
        return {"errors": form.errors}, 400


@recipe.route('/<int:recipeId>/ratings', methods=['POST'])
@login_required
def post_rating(recipeId):
    """
    route that validates data and creates a new rating
    """

    form = RatingForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        newRating = Rating(
            recipe_id = data['recipe_id'],
            user_id = data['user_id'],
            rating = data['rating']
        )

        db.session.add(newRating)
        db.session.commit()

        return newRating.to_dict()

    else:
        return {"errors": form.errors}, 400


@recipe.route('/<int:recipeId>/save', methods=['POST'])
@login_required
def save_recipe(recipeId):
    """
    Route that saves a recipe to the user's saved recipes
    """

    userId = int(session['_user_id'])

    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)

    user.saved_recipes.append(recipe)
    db.session.commit()

    return user.to_dict()


@recipe.route('/<int:recipeId>/unsave', methods=['DELETE'])
@login_required
def unsave_recipe(recipeId):
    """
    Route that removes a recipe from the user's saved recipes
    """

    userId = int(session['_user_id'])

    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)

    user.saved_recipes.remove(recipe)
    db.session.commit()

    return user.to_dict()

@recipe.route('/<int:recipeId>/cooked', methods=['POST'])
@login_required
def set_recipe_cooked (recipeId):
    """
    Route that adds a recipe to the user's cooked recipes
    """

    userId = int(session['_user_id'])

    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)

    user.cooked_recipes.append(recipe)
    db.session.commit()

    return {
        "message": f"recipe '{recipeId}' successfully added to cooked recipes for user '{userId}'"
    }

@recipe.route('<int:recipeId>/remove-cooked', methods=['DELETE'])
@login_required
def remove_cooked_recipe (recipeId):
    """
    Route that removes a recipe from the user's cooked recipes
    """

    userId = int(session["_user_id"])

    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)

    user.cooked_recipes.remove(recipe)
    db.session.commit()

    return {
        "message": f"recipe '{recipeId}' successfully removed from cooked recipes for user '{userId}'"
    }
