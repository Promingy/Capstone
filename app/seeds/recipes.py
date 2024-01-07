from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds Demo recipes to the db
def seed_recipes():
    """
    Func that addes pre-seeded recipes to the database
    """

    Recipe1 = Recipe(
        # id = 1,
        owner_id = 3,
        category_id = 2,
        title = "Spaghetti Bolognese",
        description = "Classic Italian pasta dish with rich meat sauce.",
        servings = 4,
        prep_time = 20,
        cook_time = 40,
        preview_image = "https://www.thevegspace.co.uk/wp-content/uploads/2015/06/FV-Insta-3.jpg",
        created_at = datetime.now()
    )

    Recipe2 = Recipe(
        # id = 2,
        owner_id = 2,
        category_id = 5,
        title = "Grilled Chicken Salad",
        description = "Healthy and delicious salad with grilled chicken breast.",
        servings = 2,
        prep_time = 15,
        cook_time = 20,
        preview_image = "https://gimmesomegrilling.com/wp-content/uploads/2021/05/Grilled-Chicken-Salad-Recipe-Square.jpg",
        created_at = datetime.now()
    )

    Recipe3 = Recipe(
        # id = 3,
        owner_id = 1,
        category_id = 7,
        title = "Vegetarian Stir-Fry",
        description = "Quick and easy stir-fry with a variety of colorful vegetables.",
        servings = 3,
        prep_time = 10,
        cook_time = 15,
        preview_image = "https://hips.hearstapps.com/hmg-prod/images/veggie-stir-fry-1597687367.jpg",
        created_at = datetime.now()
    )

    Recipe4 = Recipe(
        # id = 4,
        owner_id = 2,
        category_id = 1,
        title = "Chocolate Chip Cookies",
        description = "Classic homemade cookies with gooey chocolate chips.",
        servings = 12,
        prep_time = 15,
        cook_time = 12,
        preview_image = "https://www.modernhoney.com/wp-content/uploads/2017/11/Thin-and-Crispy-Chocolate-Chip-Cookies-2.jpg",
        created_at = datetime.now()
    )

    Recipe5 = Recipe(
        # id = 5,
        owner_id = 3,
        category_id = 3,
        title = "Tomato Basil Pasta",
        description = "Simple and flavorful pasta with fresh tomatoes and basil.",
        servings = 3,
        prep_time = 10,
        cook_time = 25,
        preview_image = "https://www.thefoodhussy.com/wp-content/uploads/2023/02/Cheesecake-Factory-Tomato-Basil-Pasta-7.jpg",
        created_at = datetime.now()
    )

    recipes = [Recipe1, Recipe2, Recipe3, Recipe4, Recipe5]

    [db.session.add(recipe) for recipe in recipes]
    db.session.commit()

def undo_recipes():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM recipes'))

    db.session.commit()
