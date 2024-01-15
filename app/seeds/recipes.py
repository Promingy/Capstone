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

    recipe16 = Recipe(
        owner_id=1,
        category_id=1,
        title="Spinach Artichoke Dip",
        description="Creamy and cheesy dip with spinach and artichokes, perfect for sharing.",
        servings=6,
        prep_time=20,
        cook_time=25,
        preview_image="https://www.onceuponachef.com/images/2022/11/spinach-artichoke-dip-1-2.jpg",
        created_at=datetime(2023, 8, 11, 14, 30)
    )

    recipe17 = Recipe(
        owner_id=2,
        category_id=2,
        title="Chicken Alfredo",
        description="Delicious creamy Alfredo sauce with grilled chicken served over pasta.",
        servings=4,
        prep_time=15,
        cook_time=30,
        preview_image="https://www.budgetbytes.com/wp-content/uploads/2022/07/Chicken-Alfredo-above.jpg",
        created_at=datetime(2023, 8, 12, 18, 45)
    )

    recipe18 = Recipe(
        owner_id=3,
        category_id=3,
        title="Chocolate Mousse",
        description="Silky and indulgent chocolate mousse, a delightful dessert for chocolate lovers.",
        servings=4,
        prep_time=20,
        cook_time=0,
        preview_image="https://bakerbynature.com/wp-content/uploads/2023/08/Easy-Chocolate-Mousse-Baker-by-Nature-12636.jpg",
        created_at=datetime(2023, 8, 13, 12, 15)
    )

    recipe19 = Recipe(
        owner_id=4,
        category_id=4,
        title="Caesar Salad",
        description="Classic Caesar salad with crisp romaine lettuce, croutons, and Caesar dressing.",
        servings=2,
        prep_time=10,
        cook_time=0,
        preview_image="https://www.spendwithpennies.com/wp-content/uploads/2023/06/1200-Caesar-Salad-Recipe-SpendWithPennies.jpg",
        created_at=datetime(2023, 8, 14, 9, 30)
    )

    recipe20 = Recipe(
        owner_id=5,
        category_id=5,
        title="Tomato Basil Soup",
        description="Comforting tomato basil soup with a hint of garlic and herbs.",
        servings=4,
        prep_time=15,
        cook_time=25,
        preview_image="https://carlsbadcravings.com/wp-content/uploads/2014/02/Parmesan-Tomato-Basil-Soup-7.jpg",
        created_at=datetime(2023, 8, 15, 15, 0)
    )

    recipe21 = Recipe(
        owner_id=6,
        category_id=7,
        title="Mushroom Risotto",
        description="Creamy and flavorful risotto with sautéed mushrooms and Parmesan cheese.",
        servings=4,
        prep_time=15,
        cook_time=30,
        preview_image="https://cdn77-s3.lazycatkitchen.com/wp-content/uploads/2019/11/vegan-mushroom-risotto-close-1000x1500.jpg",
        created_at=datetime(2023, 8, 16, 11, 45)
    )

    recipe22 = Recipe(
        owner_id=7,
        category_id=7,
        title="Vegetarian Pizza",
        description="Delicious pizza topped with a variety of fresh vegetables and melted cheese.",
        servings=3,
        prep_time=20,
        cook_time=15,
        preview_image="https://www.eatingwell.com/thmb/PhRj8Sp6g5m-Cn9AJL2zeLi1LM4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/easy-vegan-pizza-1x1-002-a224f13696b3483d8099b7ae5b494250.jpg",
        created_at=datetime(2023, 8, 17, 14, 20)
    )

    recipe23 = Recipe(
        owner_id=10,
        category_id=7,
        title="Stuffed Zucchini Boats",
        description="Zucchini halves filled with a savory mixture of quinoa, black beans, corn, tomatoes, and spices.",
        servings=4,
        prep_time=20,
        cook_time=25,
        preview_image="https://www.tasteandtellblog.com/wp-content/uploads/2023/07/Stuffed-Zucchini-Boats-6.jpg",
        created_at=datetime(2023, 8, 20, 10, 15)
    )

    recipe24 = Recipe(
        owner_id=9,
        category_id=7,
        title="Stuffed Bell Peppers",
        description="Bell peppers stuffed with a mixture of rice, black beans, corn, and spices.",
        servings=5,
        prep_time=25,
        cook_time=35,
        preview_image="https://www.vindulge.com/wp-content/uploads/2020/04/Stuffed-Peppers-with-Ground-Beef-Cooked-on-the-Grill.jpg",
        created_at=datetime(2023, 8, 19, 16, 30)
    )

    recipe25 = Recipe(
        owner_id=10,
        category_id=2,
        title="Pesto Chicken Pasta",
        description="Grilled chicken breast tossed with al dente pasta and a flavorful basil pesto sauce.",
        servings=2,
        prep_time=20,
        cook_time=15,
        preview_image="https://www.sipandfeast.com/wp-content/uploads/2022/05/chicken-pesto-pasta-salad-recipe-snippet.jpg",
        created_at=datetime(2023, 8, 20, 18, 30)
    )
    
    recipe26 = Recipe(
        owner_id=1,
        category_id=1,
        title="Caprese Skewers",
        description="Fresh mozzarella, cherry tomatoes, and basil leaves skewered and drizzled with balsamic glaze.",
        servings=4,
        prep_time=15,
        cook_time=1,
        preview_image="https://www.mashed.com/img/gallery/easy-caprese-skewers-recipe/l-intro-1626782645.jpg",
        created_at=datetime(2023, 8, 21, 12, 30)
    )

    recipe27 = Recipe(
        owner_id=2,
        category_id=1,
        title="Stuffed Mushrooms",
        description="Mushroom caps stuffed with a savory mixture of breadcrumbs, garlic, herbs, and cream cheese.",
        servings=5,
        prep_time=20,
        cook_time=20,
        preview_image="https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2021/11/Stuffed-Mushrooms-main-1-1.jpg",
        created_at=datetime(2023, 8, 22, 9, 15)
    )

    recipe28 = Recipe(
        owner_id=3,
        category_id=1,
        title="Bacon-Wrapped Jalapeño Poppers",
        description="Spicy jalapeño peppers filled with cream cheese, wrapped in bacon, and baked until crispy.",
        servings=6,
        prep_time=15,
        cook_time=25,
        preview_image="https://www.jerkyholic.com/wp-content/uploads/2023/05/finaljalapenopoppers.jpg",
        created_at=datetime(2023, 8, 23, 15, 45)
    )

    recipe29 = Recipe(
        owner_id=4,
        category_id=3,
        title="Chocolate Lava Cake",
        description="Decadent chocolate cake with a gooey molten chocolate center. Served with a scoop of vanilla ice cream.",
        servings=2,
        prep_time=15,
        cook_time=12,
        preview_image="https://nomnompaleo.com/wp-content/uploads/2021/02/800-LavaCakes-aaDSC_9507.jpg",
        created_at=datetime(2023, 8, 24, 20, 0)
    )

    recipe30 = Recipe(
        owner_id=5,
        category_id=3,
        title="Strawberry Shortcake",
        description="Layers of sweet sponge cake, fresh strawberries, and whipped cream. A classic dessert for summer.",
        servings=8,
        prep_time=25,
        cook_time=15,
        preview_image="https://iambaker.net/wp-content/uploads/2023/05/strawberry-shortcake-cake-1.jpg",
        created_at=datetime(2023, 8, 25, 17, 30)
    )

    recipe31 = Recipe(
        owner_id=6,
        category_id=5,
        title="Minestrone Soup",
        description="A hearty Italian soup with a variety of vegetables, beans, and pasta.",
        servings=6,
        prep_time=15,
        cook_time=40,
        preview_image="https://www.aberdeenskitchen.com/wp-content/uploads/2019/10/Easy-Classic-Minestrone-Soup-1-FI-Thumbnail-1200X1200.jpg",
        created_at=datetime(2023, 8, 26, 11, 0)
    )

    recipe32 = Recipe(
        owner_id=7,
        category_id=5,
        title="Chicken Noodle Soup",
        description="Classic comfort soup with chicken, vegetables, and egg noodles.",
        servings=4,
        prep_time=20,
        cook_time=30,
        preview_image="https://www.bigbearswife.com/wp-content/uploads/2020/05/30-Minute-Pantry-Chicken-Noodle-Soup-3-735x1029.png",
        created_at=datetime(2023, 8, 27, 14, 45)
    )

    recipe33 = Recipe(
        owner_id=8,
        category_id=5,
        title="Potato Leek Soup",
        description="Creamy soup made with potatoes, leeks, onions, and a touch of cream.",
        servings=5,
        prep_time=20,
        cook_time=35,
        preview_image="https://www.feastingathome.com/wp-content/uploads/2014/10/best-potato-leek-soup-recipe-7.jpg",
        created_at=datetime(2023, 8, 28, 9, 30)
    )

    recipe34 = Recipe(
        owner_id=9,
        category_id=10,
        title="Homemade Trail Mix",
        description="A mix of nuts, dried fruits, and chocolate for a quick and energy-boosting snack.",
        servings=10,
        prep_time=5,
        cook_time=1,
        preview_image="https://www.freshoffthegrid.com/wp-content/uploads/sriracha-trail-mix-spicy-gluten-free.jpg",
        created_at=datetime(2023, 8, 29, 16, 15)
    )

    recipe35 = Recipe(
        owner_id=10,
        category_id=10,
        title="Cucumber Slices with Hummus",
        description="Sliced cucumbers served with creamy hummus. A light and refreshing snack.",
        servings=4,
        prep_time=10,
        cook_time=1,
        preview_image="https://blog.fatfreevegan.com/wp-content/uploads/2010/08/cucumber-hummus-fb.jpg",
        created_at=datetime(2023, 8, 30, 12, 0)
    )

    recipes = [
            Recipe1, Recipe2, Recipe3, Recipe4, Recipe5,
            recipe6, recipe7, recipe8, recipe9, recipe10,
            recipe11, recipe12, recipe13, recipe14, recipe15,
            recipe16, recipe17, recipe18, recipe19, recipe20,
            recipe21, recipe22, recipe23, recipe24, recipe25,
            recipe26, recipe27, recipe28, recipe29, recipe30,
            recipe31, recipe32, recipe33, recipe34, recipe35
        ]

    [db.session.add(recipe) for recipe in recipes]
    db.session.commit()

def undo_recipes():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM recipes'))

    db.session.commit()
