from app.models import db, environment, Quantity, SCHEMA
from sqlalchemy.sql import text

def seed_quantities():
    """
    Func that adds pre-seeded quantities for recipes to the database
    """
    quantity1 = Quantity(
        recipe_id=1,
        ingredient_measurement_id=8,
        ingredient="Spaghetti",
        ingredient_quantity=300
    )

    quantity2 = Quantity(
        recipe_id=1,
        ingredient_measurement_id=7,
        ingredient="Ground Beef",
        ingredient_quantity=500
    )

    quantity3 = Quantity(
        recipe_id=1,
        ingredient_measurement_id=1,
        ingredient="Tomato Sauce",
        ingredient_quantity=400
    )

    quantity4 = Quantity(
        recipe_id=2,
        ingredient_measurement_id=6,
        ingredient="Chicken Breast",
        ingredient_quantity=250
    )

    quantity5 = Quantity(
        recipe_id=2,
        ingredient_measurement_id=7,
        ingredient="Lettuce",
        ingredient_quantity=150
    )

    quantity6 = Quantity(
        recipe_id=2,
        ingredient_measurement_id=1,
        ingredient="Cherry Tomatoes",
        ingredient_quantity=200
    )

    quantity7 = Quantity(
        recipe_id=3,
        ingredient_measurement_id=8,
        ingredient="Broccoli",
        ingredient_quantity=300
    )

    quantity8 = Quantity(
        recipe_id=3,
        ingredient_measurement_id=8,
        ingredient="Carrots",
        ingredient_quantity=200
    )

    quantity9 = Quantity(
        recipe_id=3,
        ingredient_measurement_id=1,
        ingredient="Soy Sauce",
        ingredient_quantity=50
    )

    quantity10 = Quantity(
        recipe_id=4,
        ingredient_measurement_id=8,
        ingredient="All-Purpose Flour",
        ingredient_quantity=200
    )

    quantity11 = Quantity(
        recipe_id=4,
        ingredient_measurement_id=7,
        ingredient="Butter",
        ingredient_quantity=150
    )

    quantity12 = Quantity(
        recipe_id=4,
        ingredient_measurement_id=6,
        ingredient="Chocolate Chips",
        ingredient_quantity=200
    )

    quantity13 = Quantity(
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Penne Pasta",
        ingredient_quantity=250
    )

    quantity14 = Quantity(
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Tomatoes",
        ingredient_quantity=300
    )

    quantity15 = Quantity(
        recipe_id=5,
        ingredient_measurement_id=8,
        ingredient="Fresh Basil",
        ingredient_quantity=20
    )
    # Recipe 6
    quantity16 = Quantity(
        recipe_id=6,
        ingredient_measurement_id=6,
        ingredient="All-Purpose Flour",
        ingredient_quantity=200
    )

    quantity17 = Quantity(
        recipe_id=6,
        ingredient_measurement_id=7,
        ingredient="Granulated Sugar",
        ingredient_quantity=150
    )

    quantity18 = Quantity(
        recipe_id=6,
        ingredient_measurement_id=6,
        ingredient="Cocoa Powder",
        ingredient_quantity=50
    )

    # Recipe 7
    quantity19 = Quantity(
        recipe_id=7,
        ingredient_measurement_id=5,
        ingredient="Tomatoes",
        ingredient_quantity=500
    )

    quantity20 = Quantity(
        recipe_id=7,
        ingredient_measurement_id=2,
        ingredient="Fresh Mozzarella",
        ingredient_quantity=1
    )

    quantity21 = Quantity(
        recipe_id=7,
        ingredient_measurement_id=6,
        ingredient="Fresh Basil",
        ingredient_quantity=0.5
    )

    # Recipe 8
    quantity22 = Quantity(
        recipe_id=8,
        ingredient_measurement_id=3,
        ingredient="Tomatoes",
        ingredient_quantity=800
    )

    quantity23 = Quantity(
        recipe_id=8,
        ingredient_measurement_id=8,
        ingredient="Heavy Cream",
        ingredient_quantity=200
    )

    quantity24 = Quantity(
        recipe_id=8,
        ingredient_measurement_id=9,
        ingredient="Fresh Basil",
        ingredient_quantity=20
    )

    # Recipe 9
    quantity25 = Quantity(
        recipe_id=9,
        ingredient_measurement_id=6,
        ingredient="Salmon Fillets",
        ingredient_quantity=2
    )

    quantity26 = Quantity(
        recipe_id=9,
        ingredient_measurement_id=1,
        ingredient="Lemon",
        ingredient_quantity=1
    )

    quantity27 = Quantity(
        recipe_id=9,
        ingredient_measurement_id=9,
        ingredient="Fresh Dill",
        ingredient_quantity=10
    )

    # Recipe 10
    quantity28 = Quantity(
        recipe_id=10,
        ingredient_measurement_id=10,
        ingredient="Mango",
        ingredient_quantity=2
    )

    quantity29 = Quantity(
        recipe_id=10,
        ingredient_measurement_id=10,
        ingredient="Avocado",
        ingredient_quantity=1
    )

    quantity30 = Quantity(
        recipe_id=10,
        ingredient_measurement_id=1,
        ingredient="Lime",
        ingredient_quantity=1
    )

    # Recipe 11
    quantity31 = Quantity(
        recipe_id=11,
        ingredient_measurement_id=10,
        ingredient="Blueberries",
        ingredient_quantity=1
    )

    quantity32 = Quantity(
        recipe_id=11,
        ingredient_measurement_id=6,
        ingredient="Greek Yogurt",
        ingredient_quantity=1
    )

    quantity33 = Quantity(
        recipe_id=11,
        ingredient_measurement_id=1,
        ingredient="Honey",
        ingredient_quantity=1
    )

    # Recipe 12
    quantity34 = Quantity(
        recipe_id=12,
        ingredient_measurement_id=8,
        ingredient="Quinoa",
        ingredient_quantity=1
    )

    quantity35 = Quantity(
        recipe_id=12,
        ingredient_measurement_id=8,
        ingredient="Broccoli",
        ingredient_quantity=200
    )

    quantity36 = Quantity(
        recipe_id=12,
        ingredient_measurement_id=8,
        ingredient="Bell Pepper",
        ingredient_quantity=150
    )

    # Recipe 13
    quantity37 = Quantity(
        recipe_id=13,
        ingredient_measurement_id=10,
        ingredient="Avocado",
        ingredient_quantity=2
    )

    quantity38 = Quantity(
        recipe_id=13,
        ingredient_measurement_id=2,
        ingredient="Tomato",
        ingredient_quantity=1
    )

    quantity39 = Quantity(
        recipe_id=13,
        ingredient_measurement_id=1,
        ingredient="Lime",
        ingredient_quantity=1
    )

    # Recipe 14
    quantity40 = Quantity(
        recipe_id=14,
        ingredient_measurement_id=6,
        ingredient="All-Purpose Flour",
        ingredient_quantity=150
    )

    quantity41 = Quantity(
        recipe_id=14,
        ingredient_measurement_id=7,
        ingredient="Granulated Sugar",
        ingredient_quantity=300
    )

    quantity42 = Quantity(
        recipe_id=14,
        ingredient_measurement_id=7,
        ingredient="Butter",
        ingredient_quantity=200
    )

    # Recipe 15
    quantity43 = Quantity(
        recipe_id=15,
        ingredient_measurement_id=8,
        ingredient="Black Beans",
        ingredient_quantity=1
    )

    quantity44 = Quantity(
        recipe_id=15,
        ingredient_measurement_id=8,
        ingredient="Rice",
        ingredient_quantity=1
    )

    quantity45 = Quantity(
        recipe_id=15,
        ingredient_measurement_id=5,
        ingredient="Tomatoes",
        ingredient_quantity=200
    )

    # Quantities for Recipe 16
    quantity46 = Quantity(
        recipe_id=16,
        ingredient_measurement_id=7,
        ingredient="cream cheese",
        ingredient_quantity=8
    )
    quantity47 = Quantity(
        recipe_id=16,
        ingredient_measurement_id=6,
        ingredient="mayonnaise",
        ingredient_quantity=1
    )
    quantity48 = Quantity(
        recipe_id=16,
        ingredient_measurement_id=6,
        ingredient="sour cream",
        ingredient_quantity=1
    )
    quantity49 = Quantity(
        recipe_id=16,
        ingredient_measurement_id=8,
        ingredient="parmesan cheese",
        ingredient_quantity=0.5
    )
    quantity50 = Quantity(
        recipe_id=16,
        ingredient_measurement_id=9,
        ingredient="artichoke hearts",
        ingredient_quantity=1
    )

    # Quantities for Recipe 17
    quantity51 = Quantity(
        recipe_id=17,
        ingredient_measurement_id=9,
        ingredient="chicken breasts",
        ingredient_quantity=2
    )
    quantity52 = Quantity(
        recipe_id=17,
        ingredient_measurement_id=2,
        ingredient="fettuccine pasta",
        ingredient_quantity=8
    )
    quantity53 = Quantity(
        recipe_id=17,
        ingredient_measurement_id=8,
        ingredient="butter",
        ingredient_quantity=0.5
    )
    quantity54 = Quantity(
        recipe_id=17,
        ingredient_measurement_id=10,
        ingredient="heavy cream",
        ingredient_quantity=1
    )
    quantity55 = Quantity(
        recipe_id=17,
        ingredient_measurement_id=10,
        ingredient="parmesan cheese (grated)",
        ingredient_quantity=0.5
    )
    # Quantities for Recipe 18
    quantity56 = Quantity(
        recipe_id=18,
        ingredient_measurement_id=6,
        ingredient="heavy cream",
        ingredient_quantity=1
    )
    quantity57 = Quantity(
        recipe_id=18,
        ingredient_measurement_id=10,
        ingredient="semi-sweet chocolate",
        ingredient_quantity=8
    )
    quantity58 = Quantity(
        recipe_id=18,
        ingredient_measurement_id=9,
        ingredient="egg yolks",
        ingredient_quantity=4
    )
    quantity59 = Quantity(
        recipe_id=18,
        ingredient_measurement_id=10,
        ingredient="granulated sugar",
        ingredient_quantity=2
    )
    quantity60 = Quantity(
        recipe_id=18,
        ingredient_measurement_id=1,
        ingredient="vanilla extract",
        ingredient_quantity=1
    )
    # Quantities for Recipe 19
    quantity61 = Quantity(
        recipe_id=19,
        ingredient_measurement_id=4,
        ingredient="romaine lettuce (chopped)",
        ingredient_quantity=1
    )
    quantity62 = Quantity(
        recipe_id=19,
        ingredient_measurement_id=5,
        ingredient="croutons",
        ingredient_quantity=0.5
    )
    quantity63 = Quantity(
        recipe_id=19,
        ingredient_measurement_id=10,
        ingredient="parmesan cheese (grated)",
        ingredient_quantity=0.25
    )
    quantity64 = Quantity(
        recipe_id=19,
        ingredient_measurement_id=9,
        ingredient="caesar dressing",
        ingredient_quantity=0.5
    )
    quantity65 = Quantity(
        recipe_id=19,
        ingredient_measurement_id=10,
        ingredient="black pepper",
        ingredient_quantity=0.25
    )

    # Quantities for Recipe 20
    quantity66 = Quantity(
        recipe_id=20,
        ingredient_measurement_id=6,
        ingredient="onion (chopped)",
        ingredient_quantity=1
    )
    quantity67 = Quantity(
        recipe_id=20,
        ingredient_measurement_id=6,
        ingredient="garlic (minced)",
        ingredient_quantity=2
    )
    quantity68 = Quantity(
        recipe_id=20,
        ingredient_measurement_id=5,
        ingredient="carrots (chopped)",
        ingredient_quantity=2
    )
    quantity69 = Quantity(
        recipe_id=20,
        ingredient_measurement_id=5,
        ingredient="celery (chopped)",
        ingredient_quantity=2
    )
    quantity70 = Quantity(
        recipe_id=20,
        ingredient_measurement_id=9,
        ingredient="canned crushed tomatoes",
        ingredient_quantity=28
    )


    quantities = [
        quantity1, quantity2, quantity3, quantity4, quantity5,
        quantity6, quantity7, quantity8, quantity9, quantity10,
        quantity11, quantity12, quantity13, quantity14, quantity15,
        quantity16, quantity17, quantity18, quantity19, quantity20,
        quantity21, quantity22, quantity23, quantity24, quantity25,
        quantity26, quantity27, quantity28, quantity29, quantity30,
        quantity31, quantity32, quantity33, quantity34, quantity35,
        quantity36, quantity37, quantity38, quantity39, quantity40,
        quantity41, quantity42, quantity43, quantity44, quantity45,
        quantity46, quantity47, quantity48, quantity49, quantity50,
        quantity51, quantity52, quantity53, quantity54, quantity55,
        quantity56, quantity57, quantity58, quantity59, quantity60,
        quantity61, quantity62, quantity63, quantity64, quantity65,
        quantity66, quantity67, quantity68, quantity69, quantity70
    ]


    [db.session.add(quantity) for quantity in quantities]
    db.session.commit()


def undo_quantities():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.quantities RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM quantities'))

    db.session.commit()
