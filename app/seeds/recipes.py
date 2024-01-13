from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds Demo recipes to the db
def seed_recipes():
    """
    Func that addes pre-seeded recipes to the database
    """

    Recipe1 = Recipe(
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
        owner_id = 2,
        category_id = 4,
        title = "Grilled Chicken Salad",
        description = "Healthy and delicious salad with grilled chicken breast.",
        servings = 2,
        prep_time = 15,
        cook_time = 20,
        preview_image = "https://gimmesomegrilling.com/wp-content/uploads/2021/05/Grilled-Chicken-Salad-Recipe-Square.jpg",
        created_at = datetime.now()
    )

    Recipe3 = Recipe(
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
        owner_id = 2,
        category_id = 3,
        title = "Chocolate Chip Cookies",
        description = "Classic homemade cookies with gooey chocolate chips.",
        servings = 12,
        prep_time = 15,
        cook_time = 12,
        preview_image = "https://www.modernhoney.com/wp-content/uploads/2017/11/Thin-and-Crispy-Chocolate-Chip-Cookies-2.jpg",
        created_at = datetime.now()
    )

    Recipe5 = Recipe(
        owner_id = 3,
        category_id = 2,
        title = "Tomato Basil Pasta",
        description = "Simple and flavorful pasta with fresh tomatoes and basil.",
        servings = 3,
        prep_time = 10,
        cook_time = 25,
        preview_image = "https://www.thefoodhussy.com/wp-content/uploads/2023/02/Cheesecake-Factory-Tomato-Basil-Pasta-7.jpg",
        created_at = datetime.now()
    )

    recipe6 = Recipe(
        owner_id=4,
        category_id=3,
        title="Classic Chocolate Cake",
        description="Indulge in the rich and moist goodness of this classic chocolate cake.",
        servings=8,
        prep_time=25,
        cook_time=35,
        preview_image="https://i0.wp.com/bethcakes.com/wp-content/uploads/2021/05/choc-cake-2.jpg",
        created_at=datetime(2023, 8, 1, 12, 30)
    )

    recipe7 = Recipe(
        owner_id=9,
        category_id=4,
        title="Caprese Salad",
        description="A refreshing salad featuring tomatoes, fresh mozzarella, and basil, drizzled with balsamic glaze.",
        servings=4,
        prep_time=15,
        cook_time=1,
        preview_image="https://www.cookinwithmima.com/wp-content/uploads/2021/08/Caprese-Salad-3.jpg",
        created_at=datetime(2023, 8, 2, 15, 45)

    )

    recipe8 = Recipe(
        owner_id=6,
        category_id=5,
        title="Creamy Tomato Basil Soup",
        description="Warm up with a bowl of this comforting creamy tomato basil soup, perfect for chilly days.",
        servings=6,
        prep_time=10,
        cook_time=30,
        preview_image="https://sharedappetite.com/wp-content/uploads/2017/04/8530112959_5515654e3c-2.jpg",
        created_at=datetime(2023, 8, 3, 10, 0)
    )

    recipe9 = Recipe(
        owner_id=1,
        category_id=2,
        title="Grilled Salmon with Lemon and Dill",
        description="Delicious grilled salmon seasoned with fresh lemon and dill for a burst of flavor.",
        servings=2,
        prep_time=15,
        cook_time=20,
        preview_image="https://www.allrecipes.com/thmb/u3LItZpJda3_FX38_78XB4m2bS0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6637559-cedar-plank-grilled-salmon-with-garlic-lemon-and-dill-Mackenzie-Schieck-4x3-1-aa9c00cd2c20464aa76e87f4d9cc6336.jpg",
        created_at=datetime(2023, 8, 4, 18, 30)
    )

    recipe10 = Recipe(
        owner_id=8,
        category_id=4,
        title="Mango Avocado Salad",
        description="A tropical salad featuring ripe mangoes, creamy avocados, and a zesty lime dressing.",
        servings=3,
        prep_time=10,
        cook_time=1,
        preview_image="https://www.lastingredient.com/wp-content/uploads/2022/05/mango-salad-with-avocado2.jpg",
        created_at=datetime(2023, 8, 5, 9, 15)
    )

    # Recipe 11
    recipe11 = Recipe(
        owner_id=3,
        category_id=6,
        title="Blueberry Smoothie",
        description="Start your day with a refreshing and antioxidant-rich blueberry smoothie.",
        servings=1,
        prep_time=5,
        cook_time=1,
        preview_image="https://www.dinneratthezoo.com/wp-content/uploads/2018/05/blueberry-smoothie-5.jpg",
        created_at=datetime(2023, 8, 6, 7, 45)
    )

    recipe12 = Recipe(
        owner_id=5,
        category_id=4,
        title="Quinoa Salad with Roasted Vegetables",
        description="A nutritious and colorful quinoa salad featuring a variety of roasted vegetables.",
        servings=4,
        prep_time=20,
        cook_time=25,
        preview_image="https://twokooksinthekitchen.com/wp-content/uploads/2023/05/roasted-vegetable-salad-with-quinoa-46.jpg",
        created_at=datetime(2023, 8, 7, 14, 20)
    )

    # Recipe 13
    recipe13 = Recipe(
        owner_id=2,
        category_id=1,
        title="Guacamole and Chips",
        description="A classic and tasty guacamole served with crisp tortilla chips.",
        servings=6,
        prep_time=15,
        cook_time=1,
        preview_image="https://thrivinghomeblog.com/wp-content/uploads/2022/01/Chips-and-Guacamole-3.jpg",
        created_at=datetime(2023, 8, 8, 11, 10)
    )

    recipe14 = Recipe(
        owner_id=7,
        category_id=10,
        title="Lemon Bars",
        description="Enjoy the perfect balance of sweet and tart with these delightful homemade lemon bars.",
        servings=12,
        prep_time=20,
        cook_time=30,
        preview_image="https://www.foodnetwork.com/content/dam/images/food/fullset/2009/5/11/0/0105037_Lemon-square_s4x3.jpg",
        created_at=datetime(2023, 8, 9, 16, 45)
    )

    recipe15 = Recipe(
        owner_id=10,
        category_id=7,
        title="Vegetarian Burrito Bowl",
        description="A hearty and nutritious burrito bowl with black beans, rice, and fresh vegetables.",
        servings=4,
        prep_time=15,
        cook_time=20,
        preview_image="https://healthyfitnessmeals.com/wp-content/uploads/2022/08/Vegetarian-burrito-bowl-5.jpg",
        created_at=datetime(2023, 8, 10, 8, 30)
    )

    recipes = [
        Recipe1, Recipe2, Recipe3, Recipe4, Recipe5,
        recipe6, recipe7, recipe8, recipe9, recipe10,
        recipe11, recipe12, recipe13, recipe14, recipe15
        ]

    [db.session.add(recipe) for recipe in recipes]
    db.session.commit()

def undo_recipes():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM recipes'))

    db.session.commit()
