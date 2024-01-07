from app.models import db, environment, Quantity, SCHEMA
from sqlalchemy.sql import text

def seed_quantities():
    """
    Func that adds pre-seeded quantities for recipes to the database
    """
    quantity1 = Quantity(
        # id=1,
        recipe_id=1,
        ingredient_measurement_id=8,
        ingredient="Spaghetti",
        ingredient_quantity=300
    )

    quantity2 = Quantity(
        # id=2,
        recipe_id=1,
        ingredient_measurement_id=7,
        ingredient="Ground Beef",
        ingredient_quantity=500
    )

    quantity3 = Quantity(
        # id=3,
        recipe_id=1,
        ingredient_measurement_id=1,
        ingredient="Tomato Sauce",
        ingredient_quantity=400
    )

    quantity4 = Quantity(
        # id=4,
        recipe_id=2,
        ingredient_measurement_id=6,
        ingredient="Chicken Breast",
        ingredient_quantity=250
    )

    quantity5 = Quantity(
        # id=5,
        recipe_id=2,
        ingredient_measurement_id=7,
        ingredient="Lettuce",
        ingredient_quantity=150
    )

    quantity6 = Quantity(
        # id=6,
        recipe_id=2,
        ingredient_measurement_id=1,
        ingredient="Cherry Tomatoes",
        ingredient_quantity=200
    )

    quantity7 = Quantity(
        # id=7,
        recipe_id=3,
        ingredient_measurement_id=8,
        ingredient="Broccoli",
        ingredient_quantity=300
    )

    quantity8 = Quantity(
        # id=8,
        recipe_id=3,
        ingredient_measurement_id=8,
        ingredient="Carrots",
        ingredient_quantity=200
    )

    quantity9 = Quantity(
        # id=9,
        recipe_id=3,
        ingredient_measurement_id=1,
        ingredient="Soy Sauce",
        ingredient_quantity=50
    )

    quantity10 = Quantity(
        # id=10,
        recipe_id=4,
        ingredient_measurement_id=8,
        ingredient="All-Purpose Flour",
        ingredient_quantity=200
    )

    quantity11 = Quantity(
        # id=11,
        recipe_id=4,
        ingredient_measurement_id=7,
        ingredient="Butter",
        ingredient_quantity=150
    )

    quantity12 = Quantity(
        # id=12,
        recipe_id=4,
        ingredient_measurement_id=6,
        ingredient="Chocolate Chips",
        ingredient_quantity=200
    )

    quantity13 = Quantity(
        # id=13,
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Penne Pasta",
        ingredient_quantity=250
    )

    quantity14 = Quantity(
        # id=14,
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Tomatoes",
        ingredient_quantity=300
    )

    quantity15 = Quantity(
        # id=15,
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Fresh Basil",
        ingredient_quantity=20
    )

    quantities = [ quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7, quantity8, quantity9, quantity10, quantity11, quantity12, quantity13, quantity14, quantity15]

    [db.session.add(quantity) for quantity in quantities]
    db.session.commit()


def undo_quantities():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.quantities RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM quantities'))

    db.session.commit()
