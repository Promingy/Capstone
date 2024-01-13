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

    quantity71 = Quantity(
        recipe_id=21,
        ingredient_measurement_id=6,
        ingredient="mushrooms (sliced)",
        ingredient_quantity=2
    )

    quantity72 = Quantity(
        recipe_id=21,
        ingredient_measurement_id=8,
        ingredient="arborio rice",
        ingredient_quantity=1
    )

    quantity73 = Quantity(
        recipe_id=21,
        ingredient_measurement_id=7,
        ingredient="vegetable broth",
        ingredient_quantity=2
    )

    quantity74 = Quantity(
        recipe_id=21,
        ingredient_measurement_id=1,
        ingredient="onion (finely chopped)",
        ingredient_quantity=0.5
    )

    quantity75 = Quantity(
        recipe_id=21,
        ingredient_measurement_id=2,
        ingredient="garlic (minced)",
        ingredient_quantity=2
    )

    quantity76 = Quantity(
        recipe_id=22,
        ingredient_measurement_id=9,
        ingredient="pizza dough",
        ingredient_quantity=1
    )

    quantity77 = Quantity(
        recipe_id=22,
        ingredient_measurement_id=3,
        ingredient="tomato sauce",
        ingredient_quantity=0.5
    )

    quantity78 = Quantity(
        recipe_id=22,
        ingredient_measurement_id=4,
        ingredient="mozzarella cheese (shredded)",
        ingredient_quantity=1
    )

    quantity79 = Quantity(
        recipe_id=22,
        ingredient_measurement_id=7,
        ingredient="bell peppers (sliced)",
        ingredient_quantity=0.5
    )

    quantity80 = Quantity(
        recipe_id=22,
        ingredient_measurement_id=10,
        ingredient="black olives (sliced)",
        ingredient_quantity=0.25
    )

    quantity81 = Quantity(
        recipe_id=23,
        ingredient_measurement_id=10,
        ingredient="quinoa (cooked)",
        ingredient_quantity=1
    )

    quantity82 = Quantity(
        recipe_id=23,
        ingredient_measurement_id=9,
        ingredient="black beans (canned, drained)",
        ingredient_quantity=0.5
    )

    quantity83 = Quantity(
        recipe_id=23,
        ingredient_measurement_id=5,
        ingredient="corn kernels",
        ingredient_quantity=0.5
    )

    quantity84 = Quantity(
        recipe_id=23,
        ingredient_measurement_id=3,
        ingredient="tomatoes (diced)",
        ingredient_quantity=0.5
    )

    quantity85 = Quantity(
        recipe_id=23,
        ingredient_measurement_id=2,
        ingredient="cumin powder",
        ingredient_quantity=0.25
    )

    quantity86 = Quantity(
        recipe_id=24,
        ingredient_measurement_id=7,
        ingredient="canned chickpeas (drained)",
        ingredient_quantity=1
    )

    quantity87 = Quantity(
        recipe_id=24,
        ingredient_measurement_id=5,
        ingredient="cucumbers (diced)",
        ingredient_quantity=1
    )

    quantity88 = Quantity(
        recipe_id=24,
        ingredient_measurement_id=3,
        ingredient="cherry tomatoes (halved)",
        ingredient_quantity=0.5
    )

    quantity89 = Quantity(
        recipe_id=24,
        ingredient_measurement_id=10,
        ingredient="kalamata olives",
        ingredient_quantity=0.25
    )

    quantity90 = Quantity(
        recipe_id=24,
        ingredient_measurement_id=4,
        ingredient="feta cheese (crumbled)",
        ingredient_quantity=0.5
    )

    quantity91 = Quantity(
        recipe_id=25,
        ingredient_measurement_id=6,  # oz
        ingredient="Fettuccine Pasta",
        ingredient_quantity=8
    )

    quantity92 = Quantity(
        recipe_id=25,
        ingredient_measurement_id=8,  # oz
        ingredient="Grilled Chicken Breast",
        ingredient_quantity=12
    )

    quantity93 = Quantity(
        recipe_id=26,
        ingredient_measurement_id=9,  # count
        ingredient="Cherry Tomatoes",
        ingredient_quantity=12
    )

    quantity94 = Quantity(
        recipe_id=26,
        ingredient_measurement_id=4,  # cup
        ingredient="Fresh Mozzarella Balls",
        ingredient_quantity=1
    )

    quantity95 = Quantity(
        recipe_id=26,
        ingredient_measurement_id=5,  # cup
        ingredient="Fresh Basil Leaves",
        ingredient_quantity=1
    )

    quantity96 = Quantity(
        recipe_id=27,
        ingredient_measurement_id=7,  # oz
        ingredient="Cream Cheese",
        ingredient_quantity=8
    )

    quantity97 = Quantity(
        recipe_id=27,
        ingredient_measurement_id=6,  # oz
        ingredient="Breadcrumbs",
        ingredient_quantity=1
    )

    quantity98 = Quantity(
        recipe_id=27,
        ingredient_measurement_id=11,  # cloves
        ingredient="Garlic (minced)",
        ingredient_quantity=2
    )

    quantity99 = Quantity(
        recipe_id=28,
        ingredient_measurement_id=10,  # slices
        ingredient="Bacon",
        ingredient_quantity=12
    )

    quantity100 = Quantity(
        recipe_id=29,
        ingredient_measurement_id=6,  # oz
        ingredient="Dark Chocolate",
        ingredient_quantity=6
    )

    quantity101 = Quantity(
        recipe_id=29,
        ingredient_measurement_id=3,  # pint
        ingredient="Vanilla Ice Cream",
        ingredient_quantity=2
    )

    quantity102 = Quantity(
        recipe_id=30,
        ingredient_measurement_id=2,  # cups
        ingredient="Strawberries",
        ingredient_quantity=2
    )

    quantity103 = Quantity(
        recipe_id=31,
        ingredient_measurement_id=1,  # can
        ingredient="Cannellini Beans",
        ingredient_quantity=1
    )

    quantity104 = Quantity(
        recipe_id=31,
        ingredient_measurement_id=6,  # oz
        ingredient="Tomato Paste",
        ingredient_quantity=4
    )

    quantity105 = Quantity(
        recipe_id=31,
        ingredient_measurement_id=9,  # count
        ingredient="Carrots",
        ingredient_quantity=2
    )

    quantity106 = Quantity(
        recipe_id=32,
        ingredient_measurement_id=2,  # cups
        ingredient="Cooked Chicken",
        ingredient_quantity=2
    )

    quantity107 = Quantity(
        recipe_id=32,
        ingredient_measurement_id=5,  # cup
        ingredient="Egg Noodles",
        ingredient_quantity=1
    )

    quantity108 = Quantity(
        recipe_id=32,
        ingredient_measurement_id=9,  # count
        ingredient="Celery Stalks",
        ingredient_quantity=2
    )

    quantity109 = Quantity(
        recipe_id=33,
        ingredient_measurement_id=7,  # oz
        ingredient="Leeks",
        ingredient_quantity=8
    )

    quantity110 = Quantity(
        recipe_id=33,
        ingredient_measurement_id=8,  # oz
        ingredient="Potatoes",
        ingredient_quantity=10
    )

    quantity111 = Quantity(
        recipe_id=33,
        ingredient_measurement_id=3,  # pint
        ingredient="Heavy Cream",
        ingredient_quantity=1
    )

    quantity112 = Quantity(
        recipe_id=34,
        ingredient_measurement_id=6,  # oz
        ingredient="Mixed Nuts",
        ingredient_quantity=8
    )

    quantity113 = Quantity(
        recipe_id=34,
        ingredient_measurement_id=7,  # lb
        ingredient="Dried Fruits",
        ingredient_quantity=1
    )

    quantity114 = Quantity(
        recipe_id=34,
        ingredient_measurement_id=10,  # count
        ingredient="Chocolate Chips",
        ingredient_quantity=10
    )

    quantity115 = Quantity(
        recipe_id=35,
        ingredient_measurement_id=1,  # fluid oz
        ingredient="Olive Oil",
        ingredient_quantity=2
    )

    quantity116 = Quantity(
        recipe_id=35,
        ingredient_measurement_id=6,  # oz
        ingredient="Hummus",
        ingredient_quantity=6
    )

    quantity117 = Quantity(
        recipe_id=35,
        ingredient_measurement_id=9,  # kg
        ingredient="Cucumbers",
        ingredient_quantity=0.5
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
        quantity66, quantity67, quantity68, quantity69, quantity70,
        quantity71, quantity72, quantity73, quantity74, quantity75,
        quantity76, quantity77, quantity78, quantity79, quantity80,
        quantity81, quantity82, quantity83, quantity84, quantity85,
        quantity86, quantity87, quantity88, quantity89, quantity90,
        quantity91, quantity92, quantity93, quantity94, quantity95,
        quantity96, quantity97, quantity98, quantity99, quantity100,
        quantity101, quantity102, quantity103, quantity104, quantity105,
        quantity106, quantity107, quantity108, quantity109, quantity110,
        quantity111, quantity112, quantity113, quantity114, quantity115,
        quantity116, quantity117
    ]


    [db.session.add(quantity) for quantity in quantities]
    db.session.commit()


def undo_quantities():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.quantities RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM quantities'))

    db.session.commit()
