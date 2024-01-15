from app.models import db, environment, Step, SCHEMA
from sqlalchemy.sql import text

def seed_steps():
    """
    Func that adds pre-seeded steps for the recipes to the db
    """

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

    step133 = Step(
        recipe_id=16,
        step_number=1,
        description="Preheat the oven to 375°F."
    )

    step134 = Step(
        recipe_id=16,
        step_number=2,
        description="In a mixing bowl, combine cream cheese, mayonnaise, and sour cream."
    )

    step135 = Step(
        recipe_id=16,
        step_number=3,
        description="Add parmesan cheese and artichoke hearts, mix well."
    )

    step136 = Step(
        recipe_id=16,
        step_number=4,
        description="Transfer the mixture to a baking dish."
    )

    step137 = Step(
        recipe_id=16,
        step_number=5,
        description="Bake for 25 minutes or until the top is golden brown."
    )

    step138 = Step(
        recipe_id=17,
        step_number=1,
        description="Cook fettuccine pasta according to package instructions."
    )

    step139 = Step(
        recipe_id=17,
        step_number=2,
        description="In a pan, cook chicken breasts in butter until fully cooked."
    )

    step140 = Step(
        recipe_id=17,
        step_number=3,
        description="Slice cooked chicken."
    )

    step141 = Step(
        recipe_id=17,
        step_number=4,
        description="In the same pan, add heavy cream, parmesan cheese, and cooked fettuccine."
    )

    step142 = Step(
        recipe_id=17,
        step_number=5,
        description="Stir until the sauce thickens and coats the pasta. Serve hot."
    )

    step143 = Step(
        recipe_id=18,
        step_number=1,
        description="In a saucepan, heat heavy cream until it simmers."
    )

    step144 = Step(
        recipe_id=18,
        step_number=2,
        description="Add semi-sweet chocolate and stir until melted."
    )

    step145 = Step(
        recipe_id=18,
        step_number=3,
        description="In a separate bowl, whisk together egg yolks and granulated sugar."
    )

    step146 = Step(
        recipe_id=18,
        step_number=4,
        description="Gradually whisk the chocolate mixture into the egg yolk mixture."
    )

    step147 = Step(
        recipe_id=18,
        step_number=5,
        description="Stir in vanilla extract and pour the mixture into serving glasses. Chill before serving."
    )

    step148 = Step(
        recipe_id=19,
        step_number=1,
        description="Place chopped romaine lettuce in a large salad bowl."
    )

    step149 = Step(
        recipe_id=19,
        step_number=2,
        description="Add croutons, grated parmesan cheese, and caesar dressing."
    )

    step150 = Step(
        recipe_id=19,
        step_number=3,
        description="Toss the salad until well coated with dressing."
    )

    step151 = Step(
        recipe_id=19,
        step_number=4,
        description="Serve the salad on individual plates, garnished with black pepper."
    )

    step152 = Step(
        recipe_id=19,
        step_number=5,
        description="Enjoy the classic Caesar salad!"
    )

    step153 = Step(
        recipe_id=20,
        step_number=1,
        description="In a large pot, sauté chopped onion and minced garlic until fragrant."
    )

    step154 = Step(
        recipe_id=20,
        step_number=2,
        description="Add chopped carrots and celery, cook until vegetables are tender."
    )

    step155 = Step(
        recipe_id=20,
        step_number=3,
        description="Pour in canned crushed tomatoes and stir to combine."
    )

    step156 = Step(
        recipe_id=20,
        step_number=4,
        description="Simmer the soup for 25 minutes, allowing flavors to meld."
    )

    step157 = Step(
        recipe_id=20,
        step_number=5,
        description="Serve the tomato basil soup hot, garnished with your favorite herbs."
    )

    step60 = Step(
        recipe_id=21,
        step_number=1,
        description="In a large pan, sauté onions and garlic until softened."
    )

    step61 = Step(
        recipe_id=21,
        step_number=2,
        description="Add sliced mushrooms and cook until they release their moisture."
    )

    step62 = Step(
        recipe_id=21,
        step_number=3,
        description="Stir in arborio rice and cook for 1-2 minutes until translucent."
    )

    step63 = Step(
        recipe_id=21,
        step_number=4,
        description="Pour in vegetable broth gradually, stirring constantly until absorbed."
    )

    step64 = Step(
        recipe_id=21,
        step_number=5,
        description="Continue cooking and stirring until the rice is creamy and cooked to al dente."
    )

    step65 = Step(
        recipe_id=22,
        step_number=1,
        description="Preheat the oven to 475°F (245°C). Roll out pizza dough on a floured surface."
    )

    step66 = Step(
        recipe_id=22,
        step_number=2,
        description="Spread tomato sauce over the dough and sprinkle with shredded mozzarella cheese."
    )

    step67 = Step(
        recipe_id=22,
        step_number=3,
        description="Top with sliced bell peppers and black olives."
    )

    step68 = Step(
        recipe_id=22,
        step_number=4,
        description="Bake in the preheated oven for 12-15 minutes or until the crust is golden and cheese is melted."
    )

    step69 = Step(
        recipe_id=22,
        step_number=5,
        description="Remove from the oven, slice, and serve hot."
    )

    step70 = Step(
        recipe_id=23,
        step_number=1,
        description="Preheat the oven to 375°F (190°C)."
    )

    step71 = Step(
        recipe_id=23,
        step_number=2,
        description="Cut zucchinis in half lengthwise, and scoop out the seeds to create a hollow 'boat' shape."
    )

    step72 = Step(
        recipe_id=23,
        step_number=3,
        description="In a bowl, mix cooked quinoa, black beans, corn, diced tomatoes, and cumin powder."
    )

    step73 = Step(
        recipe_id=23,
        step_number=4,
        description="Stuff the zucchini halves with the quinoa mixture."
    )

    step74 = Step(
        recipe_id=23,
        step_number=5,
        description="Bake in the preheated oven for 20-25 minutes or until zucchinis are tender."
    )

    step75 = Step(
        recipe_id=24,
        step_number=1,
        description="In a large bowl, combine drained chickpeas, diced cucumbers, halved cherry tomatoes, kalamata olives, and crumbled feta cheese."
    )

    step76 = Step(
        recipe_id=24,
        step_number=2,
        description="Toss the ingredients together until well combined."
    )

    step77 = Step(
        recipe_id=24,
        step_number=3,
        description="Serve the Greek Chickpea Salad chilled, and enjoy!"
    )

    step78 = Step(
        recipe_id=24,
        step_number=4,
        description="Feel free to add a drizzle of olive oil and a sprinkle of oregano before serving."
    )

    step79 = Step(
        recipe_id=24,
        step_number=5,
        description="Optional: Serve with pita bread or as a side dish to your favorite main course."
    )

    step80 = Step(
        recipe_id=25,
        step_number=1,
        description="Cook fettuccine pasta according to package instructions."
    )

    step81 = Step(
        recipe_id=25,
        step_number=2,
        description="Season chicken breast with salt and pepper. Grill until cooked through."
    )

    step82 = Step(
        recipe_id=25,
        step_number=3,
        description="Slice grilled chicken into thin strips."
    )

    step83 = Step(
        recipe_id=25,
        step_number=4,
        description="Toss cooked pasta with grilled chicken and basil pesto sauce."
    )

    step84 = Step(
        recipe_id=25,
        step_number=5,
        description="Serve hot and enjoy!"
    )

    step85 = Step(
        recipe_id=26,
        step_number=1,
        description="Thread cherry tomatoes, fresh mozzarella, and basil leaves onto skewers."
    )

    step86 = Step(
        recipe_id=26,
        step_number=2,
        description="Drizzle balsamic glaze over the skewers."
    )

    step87 = Step(
        recipe_id=26,
        step_number=3,
        description="Serve immediately for a delightful appetizer."
    )

    step88 = Step(
        recipe_id=27,
        step_number=1,
        description="Preheat the oven to 375°F (190°C)."
    )

    step89 = Step(
        recipe_id=27,
        step_number=2,
        description="Clean and remove stems from mushrooms. Place caps on a baking sheet."
    )

    step90 = Step(
        recipe_id=27,
        step_number=3,
        description="In a bowl, mix cream cheese, breadcrumbs, garlic, and herbs."
    )

    step91 = Step(
        recipe_id=27,
        step_number=4,
        description="Spoon the cream cheese mixture into mushroom caps."
    )

    step92 = Step(
        recipe_id=27,
        step_number=5,
        description="Bake for 20 minutes or until mushrooms are tender."
    )

    step93 = Step(
        recipe_id=28,
        step_number=1,
        description="Preheat the oven to 375°F (190°C)."
    )

    step94 = Step(
        recipe_id=28,
        step_number=2,
        description="Slice jalapeños in half lengthwise, remove seeds and membranes."
    )

    step95 = Step(
        recipe_id=28,
        step_number=3,
        description="Fill jalapeño halves with cream cheese."
    )

    step96 = Step(
        recipe_id=28,
        step_number=4,
        description="Wrap each jalapeño with a half-slice of bacon and secure with a toothpick."
    )

    step97 = Step(
        recipe_id=28,
        step_number=5,
        description="Bake until bacon is crispy, about 25 minutes."
    )

    step98 = Step(
        recipe_id=29,
        step_number=1,
        description="Preheat the oven to 425°F (220°C). Grease and flour ramekins."
    )

    step99 = Step(
        recipe_id=29,
        step_number=2,
        description="Melt dark chocolate and butter in a double boiler."
    )

    step100 = Step(
        recipe_id=29,
        step_number=3,
        description="Whisk in sugar, eggs, and vanilla until well combined."
    )

    step101 = Step(
        recipe_id=29,
        step_number=4,
        description="Fold in flour until just combined."
    )

    step102 = Step(
        recipe_id=29,
        step_number=5,
        description="Pour batter into prepared ramekins and bake for 12 minutes."
    )

    step103 = Step(
        recipe_id=30,
        step_number=1,
        description="Prepare sponge cake according to package instructions."
    )

    step104 = Step(
        recipe_id=30,
        step_number=2,
        description="Slice strawberries and whip the cream."
    )

    step105 = Step(
        recipe_id=30,
        step_number=3,
        description="Layer sponge cake, strawberries, and whipped cream."
    )

    step106 = Step(
        recipe_id=30,
        step_number=4,
        description="Repeat layers until all ingredients are used."
    )

    step107 = Step(
        recipe_id=30,
        step_number=5,
        description="Chill in the refrigerator before serving."
    )

    step108 = Step(
        recipe_id=31,
        step_number=1,
        description="In a large pot, sauté onions and garlic until softened."
    )

    step109 = Step(
        recipe_id=31,
        step_number=2,
        description="Add diced tomatoes, broth, and Italian seasoning."
    )

    step110 = Step(
        recipe_id=31,
        step_number=3,
        description="Bring to a boil, then reduce heat and simmer for 30 minutes."
    )

    step111 = Step(
        recipe_id=31,
        step_number=4,
        description="Add beans, pasta, and spinach. Cook until pasta is tender."
    )

    step112 = Step(
        recipe_id=31,
        step_number=5,
        description="Serve hot with a sprinkle of Parmesan cheese."
    )

    step113 = Step(
        recipe_id=32,
        step_number=1,
        description="In a large pot, bring chicken broth to a simmer."
    )

    step114 = Step(
        recipe_id=32,
        step_number=2,
        description="Add diced chicken, vegetables, and egg noodles."
    )

    step115 = Step(
        recipe_id=32,
        step_number=3,
        description="Simmer until chicken is cooked and noodles are tender."
    )

    step116 = Step(
        recipe_id=32,
        step_number=4,
        description="Season with salt, pepper, and fresh herbs."
    )

    step117 = Step(
        recipe_id=32,
        step_number=5,
        description="Serve hot and comforting."
    )

    step118 = Step(
        recipe_id=33,
        step_number=1,
        description="Sauté leeks and onions in butter until softened."
    )

    step119 = Step(
        recipe_id=33,
        step_number=2,
        description="Add diced potatoes and chicken broth. Simmer until potatoes are tender."
    )

    step120 = Step(
        recipe_id=33,
        step_number=3,
        description="Puree the soup until smooth. Add cream and season with salt and pepper."
    )

    step121 = Step(
        recipe_id=33,
        step_number=4,
        description="Simmer for an additional 10 minutes."
    )

    step122 = Step(
        recipe_id=33,
        step_number=5,
        description="Garnish with fresh chives and serve."
    )

    step123 = Step(
        recipe_id=34,
        step_number=1,
        description="Mix nuts, dried fruits, and chocolate in a large bowl."
    )

    step124 = Step(
        recipe_id=34,
        step_number=2,
        description="Store the trail mix in an airtight container."
    )

    step125 = Step(
        recipe_id=34,
        step_number=3,
        description="Portion into small bags for a convenient snack."
    )

    step126 = Step(
        recipe_id=34,
        step_number=4,
        description="Enjoy on the go or as a midday pick-me-up."
    )

    step127 = Step(
        recipe_id=34,
        step_number=5,
        description="Share with friends for a healthy party snack."
    )

    step128 = Step(
        recipe_id=35,
        step_number=1,
        description="Slice cucumbers into rounds or sticks."
    )

    step129 = Step(
        recipe_id=35,
        step_number=2,
        description="Serve with a bowl of hummus for dipping."
    )

    step130 = Step(
        recipe_id=35,
        step_number=3,
        description="A refreshing and low-calorie snack option."
    )

    step131 = Step(
        recipe_id=35,
        step_number=4,
        description="Ideal for parties or afternoon munching."
    )

    step132 = Step(
        recipe_id=35,
        step_number=5,
        description="Enjoy the crispness of the cucumber with the creaminess of hummus."
    )

    steps = [
        step16, step17, step18, step19, step20,
        step21, step22, step23, step24, step25,
        step26, step27, step28, step29, step30,
        step31, step32, step33, step34, step35,
        step36, step37, step38, step39, step40,
        step41, step42, step43, step44, step45,
        step46, step47, step48, step49, step50,
        step51, step52, step53, step54, step55,
        step56, step57, step58, step59, step60,
        step61, step62, step63, step64, step65,
        step66, step67, step68, step69, step70,
        step71, step72, step73, step74, step75,
        step76, step77, step78, step79, step80,
        step81, step82, step83, step84, step85,
        step86, step87, step88, step89, step90,
        step91, step92, step93, step94, step95,
        step96, step97, step98, step99, step100,
        step101, step102, step103, step104, step105,
        step106, step107, step108, step109, step110,
        step111, step112, step113, step114, step115,
        step116, step117, step118, step119, step120,
        step121, step122, step123, step124, step125,
        step126, step127, step128, step129, step130,
        step131, step132, step133, step134, step135,
        step136, step137, step138, step139, step140,
        step141, step142, step143, step144, step145,
        step146, step147, step148, step149, step150,
        step151, step152, step153, step154, step155,
        step156, step157
    ]

    [db.session.add(step) for step in steps]
    db.session.commit()

def undo_steps():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.steps RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM steps'))

    db.session.commit()
