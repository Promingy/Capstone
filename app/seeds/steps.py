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

    steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9, step10, step11, step12, step13, step14, step15]

    [db.session.add(step) for step in steps]
    db.session.commit()

def undo_steps():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.steps RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM steps'))

    db.session.commit()
