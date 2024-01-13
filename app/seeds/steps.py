from app.models import db, environment, Step, SCHEMA
from sqlalchemy.sql import text

def seed_steps():
    """
    Func that adds pre-seeded steps for the recipes to the db
    """

    step1 = Step(
    recipe_id=1,
    step_number=1,
    description="Boil water and cook spaghetti according to package instructions."
    )

    step2 = Step(
        recipe_id=1,
        step_number=2,
        description="In a separate pan, brown ground beef until fully cooked."
    )

    step3 = Step(
        recipe_id=1,
        step_number=3,
        description="Add tomato sauce to the cooked ground beef and simmer for 10 minutes."
    )

    step4 = Step(
        recipe_id=2,
        step_number=1,
        description="Grill chicken breast until fully cooked."
    )

    step5 = Step(
        recipe_id=2,
        step_number=2,
        description="Chop lettuce and slice cherry tomatoes for the salad."
    )

    step6 = Step(
        recipe_id=2,
        step_number=3,
        description="Combine grilled chicken, lettuce, and cherry tomatoes in a large bowl."
    )

    step7 = Step(
        recipe_id=3,
        step_number=1,
        description="Cut broccoli into florets and peel and slice carrots."
    )

    step8 = Step(
        recipe_id=3,
        step_number=2,
        description="Stir-fry broccoli and carrots in a pan with soy sauce for 5 minutes."
    )

    step9 = Step(
        recipe_id=3,
        step_number=3,
        description="Continue cooking until vegetables are tender."
    )

    step10 = Step(
        recipe_id=4,
        step_number=1,
        description="Preheat oven to 350°F (175°C)."
    )

    step11 = Step(
        recipe_id=4,
        step_number=2,
        description="In a bowl, cream together butter and sugar. Add eggs and vanilla; mix well."
    )

    step12 = Step(
        recipe_id=4,
        step_number=3,
        description="In a separate bowl, combine flour, baking soda, and salt. Gradually add to the wet mixture."
    )

    step13 = Step(
        recipe_id=5,
        step_number=1,
        description="Cook penne pasta according to package instructions. Drain and set aside."
    )

    step14 = Step(
        recipe_id=5,
        step_number=2,
        description="Dice tomatoes and chop fresh basil."
    )

    step15 = Step(
        recipe_id=5,
        step_number=3,
        description="Mix cooked pasta with tomatoes and fresh basil. Serve warm."
    )
    # Recipe 1
    step16 = Step(
        recipe_id=1,
        step_number=1,
        description="Boil water and cook spaghetti according to package instructions."
    )

    step17 = Step(
        recipe_id=1,
        step_number=2,
        description="In a separate pan, brown ground beef until fully cooked."
    )

    step18 = Step(
        recipe_id=1,
        step_number=3,
        description="Add tomato sauce to the cooked ground beef and simmer for 10 minutes."
    )

    # Recipe 2
    step19 = Step(
        recipe_id=2,
        step_number=1,
        description="Grill chicken breast until fully cooked."
    )

    step20 = Step(
        recipe_id=2,
        step_number=2,
        description="Chop lettuce and slice cherry tomatoes for the salad."
    )

    step21 = Step(
        recipe_id=2,
        step_number=3,
        description="Combine grilled chicken, lettuce, and cherry tomatoes in a large bowl."
    )

    # Recipe 3
    step22 = Step(
        recipe_id=3,
        step_number=1,
        description="Cut broccoli into florets and peel and slice carrots."
    )

    step23 = Step(
        recipe_id=3,
        step_number=2,
        description="Stir-fry broccoli and carrots in a pan with soy sauce for 5 minutes."
    )

    step24 = Step(
        recipe_id=3,
        step_number=3,
        description="Continue cooking until vegetables are tender."
    )

    # Recipe 4
    step25 = Step(
        recipe_id=4,
        step_number=1,
        description="Preheat oven to 350°F (175°C)."
    )

    step26 = Step(
        recipe_id=4,
        step_number=2,
        description="In a bowl, cream together butter and sugar. Add eggs and vanilla; mix well."
    )

    step27 = Step(
        recipe_id=4,
        step_number=3,
        description="In a separate bowl, combine flour, baking soda, and salt. Gradually add to the wet mixture."
    )

    # Recipe 5
    step28 = Step(
        recipe_id=5,
        step_number=1,
        description="Cook penne pasta according to package instructions. Drain and set aside."
    )

    step29 = Step(
        recipe_id=5,
        step_number=2,
        description="Dice tomatoes and chop fresh basil."
    )

    step30 = Step(
        recipe_id=5,
        step_number=3,
        description="Mix cooked pasta with tomatoes and fresh basil. Serve warm."
    )

    # Recipe 6
    step31 = Step(
        recipe_id=6,
        step_number=1,
        description="Preheat the oven to 350°F (175°C). Grease and flour a cake pan."
    )

    step32 = Step(
        recipe_id=6,
        step_number=2,
        description="In a large bowl, sift together flour, cocoa powder, and baking soda."
    )

    step33 = Step(
        recipe_id=6,
        step_number=3,
        description="In another bowl, cream together butter and sugar until light and fluffy. Add eggs and vanilla; mix well."
    )

    # Recipe 7
    step34 = Step(
        recipe_id=7,
        step_number=1,
        description="Slice tomatoes and fresh mozzarella into rounds."
    )

    step35 = Step(
        recipe_id=7,
        step_number=2,
        description="Arrange tomato, mozzarella, and basil leaves in an alternating pattern on a serving platter."
    )

    step36 = Step(
        recipe_id=7,
        step_number=3,
        description="Drizzle balsamic glaze over the salad. Season with salt and pepper to taste."
    )

    # Recipe 8
    step37 = Step(
        recipe_id=8,
        step_number=1,
        description="In a large pot, sauté tomatoes in olive oil until softened."
    )

    step38 = Step(
        recipe_id=8,
        step_number=2,
        description="Add heavy cream and fresh basil to the pot. Simmer for 15 minutes."
    )

    step39 = Step(
        recipe_id=8,
        step_number=3,
        description="Blend the soup until smooth using an immersion blender. Season with salt and pepper."
    )

    # Recipe 9
    step40 = Step(
        recipe_id=9,
        step_number=1,
        description="Preheat the grill. Season salmon fillets with salt, pepper, and lemon juice."
    )

    step41 = Step(
        recipe_id=9,
        step_number=2,
        description="Grill salmon fillets for 4-5 minutes per side, or until the internal temperature reaches 145°F (63°C)."
    )

    step42 = Step(
        recipe_id=9,
        step_number=3,
        description="Sprinkle freshly chopped dill over grilled salmon before serving."
    )

    # Recipe 10
    step43 = Step(
        recipe_id=10,
        step_number=1,
        description="Dice mango and avocado into bite-sized pieces."
    )

    step44 = Step(
        recipe_id=10,
        step_number=2,
        description="In a bowl, combine diced mango and avocado. Squeeze lime juice over the mixture."
    )

    step45 = Step(
        recipe_id=10,
        step_number=3,
        description="Toss the salad gently and serve chilled."
    )

    # Recipe 11
    step46 = Step(
        recipe_id=11,
        step_number=1,
        description="Blend blueberries, Greek yogurt, and honey until smooth."
    )

    step47 = Step(
        recipe_id=11,
        step_number=2,
        description="Pour the smoothie into a glass and enjoy immediately."
    )

    # Recipe 12
    step48 = Step(
        recipe_id=12,
        step_number=1,
        description="Rinse quinoa under cold water. Cook quinoa according to package instructions."
    )

    step49 = Step(
        recipe_id=12,
        step_number=2,
        description="Roast broccoli and bell pepper in the oven until tender."
    )

    step50 = Step(
        recipe_id=12,
        step_number=3,
        description="In a large bowl, combine cooked quinoa, roasted vegetables, and a drizzle of olive oil. Toss to mix."
    )

    # Recipe 13
    step51 = Step(
        recipe_id=13,
        step_number=1,
        description="Mash avocados in a bowl. Add diced tomatoes and lime juice."
    )

    step52 = Step(
        recipe_id=13,
        step_number=2,
        description="Season the guacamole with salt and pepper to taste."
    )

    step53 = Step(
        recipe_id=13,
        step_number=3,
        description="Serve the guacamole with crispy tortilla chips."
    )

    # Recipe 14
    step54 = Step(
        recipe_id=14,
        step_number=1,
        description="Preheat the oven to 350°F (175°C). Grease and flour a baking pan."
    )

    step55 = Step(
        recipe_id=14,
        step_number=2,
        description="In a bowl, combine flour, sugar, and softened butter. Press the mixture into the prepared baking pan."
    )

    step56 = Step(
        recipe_id=14,
        step_number=3,
        description="Bake the crust in the preheated oven for 15 minutes, or until lightly golden."
    )

    # Recipe 15
    step57 = Step(
        recipe_id=15,
        step_number=1,
        description="Cook black beans and rice according to package instructions."
    )

    step58 = Step(
        recipe_id=15,
        step_number=2,
        description="Dice tomatoes and prepare any additional toppings of your choice."
    )

    step59 = Step(
        recipe_id=15,
        step_number=3,
        description="In a bowl, assemble the burrito bowl with black beans, rice, tomatoes, and your favorite toppings."
    )


    steps = [
        step1, step2, step3, step4, step5,
        step6, step7, step8, step9, step10,
        step11, step12, step13, step14, step15,
        step16, step17, step18, step19, step20,
        step21, step22, step23, step24, step25,
        step26, step27, step28, step29, step30,
        step31, step32, step33, step34, step35,
        step36, step37, step38, step39, step40,
        step41, step42, step43, step44, step45,
        step46, step47, step48, step49, step50,
        step51, step52, step53, step54, step55,
        step56, step57, step58, step59,
    ]


    [db.session.add(step) for step in steps]
    db.session.commit()

def undo_steps():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.steps RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM steps'))

    db.session.commit()
