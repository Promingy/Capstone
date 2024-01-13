from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime
from .users import users

user1, user2, user3,\
user4, user5, user6,\
user7, user8, user9,\
user10, user11, user12,\
user13 = users

def seed_reviews() :
    """
    function that generates reviews for all of the recipes
    """

    review1 = Review(
        user_id=1,
        recipe_id=1,
        body="Delicious dish! I loved it.",
        edited=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        review_likes = [user1, user2]
    )

    review2 = Review(
        user_id=2,
        recipe_id=2,
        body="Healthy and tasty salad.",
        edited=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        review_likes = [user2, user3]
    )

    review3 = Review(
        user_id=3,
        recipe_id=3,
        body="Quick and easy stir-fry recipe!",
        edited=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        review_likes = [user1, user3]
    )

    review4 = Review(
        user_id=1,
        recipe_id=4,
        body="Best chocolate chip cookies ever!",
        edited=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        review_likes = [user2, user3]
    )

    review5 = Review(
        user_id=2,
        recipe_id=5,
        body="Simple and delicious pasta dish.",
        edited=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        review_likes = [user1, user3]
    )

    review6 = Review(
        user_id=6,
        recipe_id=6,
        body="Absolutely delicious! The combination of flavors is a delight for the taste buds.",
        edited=False,
        created_at=datetime(2023, 9, 6, 10, 15),
        updated_at=datetime(2023, 9, 6, 10, 15),
        review_likes=[user2, user4, user7],
    )

    review7 = Review(
        user_id=7,
        recipe_id=6,
        body="Incredible dish! I shared it with friends, and they were all asking for the recipe.",
        edited=False,
        created_at=datetime(2023, 9, 7, 14, 30),
        updated_at=datetime(2023, 9, 7, 14, 30),
        review_likes=[user1, user3, user5],
    )

    review8 = Review(
        user_id=8,
        recipe_id=6,
        body="This dish exceeded my expectations. The spices used are perfect!",
        edited=False,
        created_at=datetime(2023, 9, 7, 15, 30),
        updated_at=datetime(2023, 9, 7, 15, 30),
        review_likes=[user2, user4],
    )

    review9 = Review(
        user_id=9,
        recipe_id=6,
        body="Simple to make yet so flavorful. I'll be making this again soon.",
        edited=False,
        created_at=datetime(2023, 9, 8, 21, 0),
        updated_at=datetime(2023, 9, 8, 21, 0),
        review_likes=[user1, user3],
    )

    review10 = Review(
        user_id=10,
        recipe_id=7,
        body="The combination of ingredients is outstanding! It's now one of my favorite recipes.",
        edited=False,
        created_at=datetime(2023, 9, 9, 12, 45),
        updated_at=datetime(2023, 9, 9, 12, 45),
        review_likes=[user1, user4, user6, user9, user12],
    )

    review11 = Review(
        user_id=11,
        recipe_id=7,
        body="I made this for a dinner party, and everyone loved it. Bravo!",
        edited=False,
        created_at=datetime(2023, 9, 10, 18, 30),
        updated_at=datetime(2023, 9, 10, 18, 30),
        review_likes=[user2, user5, user8],
    )

    review12 = Review(
        user_id=12,
        recipe_id=7,
        body="Simple to follow recipe with extraordinary results. Definitely a go-to dish.",
        edited=False,
        created_at=datetime(2023, 9, 11, 9, 15),
        updated_at=datetime(2023, 9, 11, 9, 15),
        review_likes=[user3, user7, user10],
    )

    review13 = Review(
        user_id=13,
        recipe_id=7,
        body="This recipe brings back childhood memories. I can't thank you enough for sharing.",
        edited=False,
        created_at=datetime(2023, 9, 12, 14, 0),
        updated_at=datetime(2023, 9, 12, 14, 0),
        review_likes=[user1, user4, user11],
    )

    review14 = Review(
        user_id=1,
        recipe_id=8,
        body="This dish is a flavor explosion! I can't wait to try more recipes from you.",
        edited=False,
        created_at=datetime(2023, 9, 13, 19, 30),
        updated_at=datetime(2023, 9, 13, 19, 30),
        review_likes=[user2, user5, user9],
    )

    review15 = Review(
        user_id=2,
        recipe_id=8,
        body="The balance of ingredients is perfect. I'll be making this again and again.",
        edited=False,
        created_at=datetime(2023, 9, 14, 16, 45),
        updated_at=datetime(2023, 9, 14, 16, 45),
        review_likes=[user3, user7, user11],
    )

    review16 = Review(
        user_id=3,
        recipe_id=8,
        body="This recipe turned a regular evening into a gourmet experience. Highly recommended!",
        edited=False,
        created_at=datetime(2023, 9, 15, 8, 15),
        updated_at=datetime(2023, 9, 15, 8, 15),
        review_likes=[user1, user4, user8],
    )

    review17 = Review(
        user_id=4,
        recipe_id=8,
        body="I love the creative twist in this dish. It's a winner for sure!",
        edited=False,
        created_at=datetime(2023, 9, 16, 12, 0),
        updated_at=datetime(2023, 9, 16, 12, 0),
        review_likes=[user2, user6, user10, user13],
    )

    review18 = Review(
        user_id=5,
        recipe_id=9,
        body="I'm impressed by how well the flavors melded together. A fantastic dish!",
        edited=False,
        created_at=datetime(2023, 9, 17, 15, 30),
        updated_at=datetime(2023, 9, 17, 15, 30),
        review_likes=[user3, user6, user9, user11],
    )

    review19 = Review(
        user_id=6,
        recipe_id=9,
        body="This recipe is a culinary masterpiece! Can't wait to explore more of your creations.",
        edited=False,
        created_at=datetime(2023, 9, 18, 10, 45),
        updated_at=datetime(2023, 9, 18, 10, 45),
        review_likes=[user2, user5, user8],
    )

    review20 = Review(
        user_id=7,
        recipe_id=9,
        body="A delightful dish that brings a burst of freshness to the table. Loving it!",
        edited=False,
        created_at=datetime(2023, 9, 19, 20, 15),
        updated_at=datetime(2023, 9, 19, 20, 15),
        review_likes=[user1, user4, user10],
    )

    review21 = Review(
        user_id=8,
        recipe_id=9,
        body="This recipe is a family favorite now. Thank you for sharing such a delicious dish!",
        edited=False,
        created_at=datetime(2023, 9, 20, 13, 0),
        updated_at=datetime(2023, 9, 20, 13, 0),
        review_likes=[user3, user7, user12],
    )

    review22 = Review(
        user_id=9,
        recipe_id=10,
        body="Absolutely amazing dish! The combination of flavors is simply divine.",
        edited=False,
        created_at=datetime(2023, 9, 21, 18, 30),
        updated_at=datetime(2023, 9, 21, 18, 30),
        review_likes=[user2, user6, user11],
    )

    review23 = Review(
        user_id=10,
        recipe_id=10,
        body="This dish is a crowd-pleaser! Easy to make and impresses every time.",
        edited=False,
        created_at=datetime(2023, 9, 22, 14, 45),
        updated_at=datetime(2023, 9, 22, 14, 45),
        review_likes=[user1, user5, user9],
    )

    review24 = Review(
        user_id=11,
        recipe_id=10,
        body="I love the vibrant colors and flavors in this dish. A true culinary delight!",
        edited=False,
        created_at=datetime(2023, 9, 23, 9, 15),
        updated_at=datetime(2023, 9, 23, 9, 15),
        review_likes=[user3, user7, user12],
    )

    review25 = Review(
        user_id=12,
        recipe_id=10,
        body="This recipe is now a family tradition. It never fails to impress!",
        edited=False,
        created_at=datetime(2023, 9, 24, 14, 0),
        updated_at=datetime(2023, 9, 24, 14, 0),
        review_likes=[user4, user8, user10],
    )

    review26 = Review(
        user_id=1,
        recipe_id=11,
        body="I'm always excited to try your recipes. This one didn't disappoint!",
        edited=False,
        created_at=datetime(2023, 9, 25, 19, 30),
        updated_at=datetime(2023, 9, 25, 19, 30),
        review_likes=[user2, user5, user9],
    )

    review27 = Review(
        user_id=2,
        recipe_id=11,
        body="The flavors in this dish are a perfect match. It's become a regular in my kitchen.",
        edited=False,
        created_at=datetime(2023, 9, 26, 16, 45),
        updated_at=datetime(2023, 9, 26, 16, 45),
        review_likes=[user3, user7, user11],
    )

    review28 = Review(
        user_id=3,
        recipe_id=11,
        body="This dish is a culinary masterpiece! The presentation and taste are top-notch.",
        edited=False,
        created_at=datetime(2023, 9, 27, 8, 15),
        updated_at=datetime(2023, 9, 27, 8, 15),
        review_likes=[user1, user4, user8],
    )

    review29 = Review(
        user_id=4,
        recipe_id=11,
        body="A delightful combination of ingredients. I'm looking forward to making it again.",
        edited=False,
        created_at=datetime(2023, 9, 28, 12, 0),
        updated_at=datetime(2023, 9, 28, 12, 0),
        review_likes=[user2, user6, user10, user13],
    )

    review30 = Review(
        user_id=5,
        recipe_id=12,
        body="This dish exceeded my expectations. The balance of flavors is superb!",
        edited=True,
        created_at=datetime(2023, 9, 29, 14, 30),
        updated_at=datetime(2023, 9, 29, 15, 0),
        review_likes=[user1, user3, user6, user12],
    )

    review31 = Review(
        user_id=6,
        recipe_id=12,
        body="I've made this recipe multiple times, and it's always a hit. Thank you!",
        edited=False,
        created_at=datetime(2023, 9, 30, 10, 45),
        updated_at=datetime(2023, 9, 30, 10, 45),
        review_likes=[user2, user5, user8],
    )

    review32 = Review(
        user_id=7,
        recipe_id=12,
        body="The presentation of this dish is as impressive as its taste. Highly recommended!",
        edited=True,
        created_at=datetime(2023, 10, 1, 20, 15),
        updated_at=datetime(2023, 10, 1, 21, 0),
        review_likes=[user3, user7, user11],
    )

    review33 = Review(
        user_id=8,
        recipe_id=12,
        body="I appreciate the simplicity of this recipe without compromising on flavor. Great job!",
        edited=False,
        created_at=datetime(2023, 10, 2, 13, 0),
        updated_at=datetime(2023, 10, 2, 13, 0),
        review_likes=[user1, user4, user9],
    )

    review34 = Review(
        user_id=9,
        recipe_id=13,
        body="I'm impressed by the depth of flavors in this recipe. Will definitely make it again!",
        edited=False,
        created_at=datetime(2023, 10, 3, 18, 30),
        updated_at=datetime(2023, 10, 3, 18, 30),
        review_likes=[user2, user5, user10],
    )

    review35 = Review(
        user_id=10,
        recipe_id=13,
        body="This dish has become a staple in my kitchen. The aroma alone is irresistible!",
        edited=True,
        created_at=datetime(2023, 10, 4, 14, 45),
        updated_at=datetime(2023, 10, 4, 15, 15),
        review_likes=[user3, user6, user11],
    )

    review36 = Review(
        user_id=11,
        recipe_id=13,
        body="I appreciate the unique combination of ingredients. It's a delightful experience.",
        edited=False,
        created_at=datetime(2023, 10, 5, 9, 15),
        updated_at=datetime(2023, 10, 5, 9, 15),
        review_likes=[user1, user4, user8],
    )

    review37 = Review(
        user_id=12,
        recipe_id=13,
        body="This recipe is a game-changer. The taste is unlike anything I've had before!",
        edited=True,
        created_at=datetime(2023, 10, 6, 14, 0),
        updated_at=datetime(2023, 10, 6, 15, 0),
        review_likes=[user2, user7, user12],
    )

    review38 = Review(
        user_id=13,
        recipe_id=14,
        body="I tried this recipe on a whim, and it turned out to be a delightful surprise. Highly recommended!",
        edited=False,
        created_at=datetime(2023, 10, 7, 19, 30),
        updated_at=datetime(2023, 10, 7, 19, 30),
        review_likes=[user1, user3, user9],
    )

    review39 = Review(
        user_id=1,
        recipe_id=14,
        body="The combination of flavors in this dish is perfect. It's now a regular in my cooking rotation.",
        edited=True,
        created_at=datetime(2023, 10, 8, 16, 45),
        updated_at=datetime(2023, 10, 8, 17, 15),
        review_likes=[user2, user5, user10],
    )

    review40 = Review(
        user_id=2,
        recipe_id=14,
        body="The simplicity of this recipe makes it a winner. I've shared it with friends who loved it too!",
        edited=False,
        created_at=datetime(2023, 10, 9, 8, 15),
        updated_at=datetime(2023, 10, 9, 8, 15),
        review_likes=[user3, user6, user11],
    )

    review41 = Review(
        user_id=3,
        recipe_id=14,
        body="This recipe is a crowd-pleaser. I've made it for family gatherings, and everyone loves it.",
        edited=True,
        created_at=datetime(2023, 10, 10, 12, 0),
        updated_at=datetime(2023, 10, 10, 13, 0),
        review_likes=[user1, user4, user8],
    )

    review42 = Review(
        user_id=4,
        recipe_id=15,
        body="I'm a fan of spicy dishes, and this one hit the spot. The heat is just right!",
        edited=False,
        created_at=datetime(2023, 10, 11, 17, 30),
        updated_at=datetime(2023, 10, 11, 17, 30),
        review_likes=[user2, user5, user9],
    )

    review43 = Review(
        user_id=5,
        recipe_id=15,
        body="The flavors in this recipe are well-balanced. It's become a regular on my dinner menu.",
        edited=True,
        created_at=datetime(2023, 10, 12, 14, 45),
        updated_at=datetime(2023, 10, 12, 15, 15),
        review_likes=[user3, user6, user10],
    )

    review44 = Review(
        user_id=6,
        recipe_id=15,
        body="The combination of ingredients in this recipe is genius. Each bite is a burst of flavor!",
        edited=False,
        created_at=datetime(2023, 10, 13, 9, 15),
        updated_at=datetime(2023, 10, 13, 9, 15),
        review_likes=[user1, user4, user11],
    )

    review45 = Review(
        user_id=7,
        recipe_id=15,
        body="I'm always looking for unique recipes, and this one is a standout. The taste is incredible.",
        edited=True,
        created_at=datetime(2023, 10, 14, 14, 0),
        updated_at=datetime(2023, 10, 14, 15, 0),
        review_likes=[user2, user7, user12],
    )

    review46 = Review(
        user_id=8,
        recipe_id=16,
        body="As a seafood lover, this dish exceeded my expectations. The freshness of the ingredients is noticeable.",
        edited=False,
        created_at=datetime(2023, 10, 15, 19, 30),
        updated_at=datetime(2023, 10, 15, 19, 30),
        review_likes=[user1, user3, user8],
    )

    review47 = Review(
        user_id=9,
        recipe_id=16,
        body="The combination of flavors in this seafood dish is divine. A must-try for seafood enthusiasts!",
        edited=True,
        created_at=datetime(2023, 10, 16, 16, 45),
        updated_at=datetime(2023, 10, 16, 17, 15),
        review_likes=[user2, user5, user10],
    )

    review48 = Review(
        user_id=10,
        recipe_id=16,
        body="I'm not usually a fan of seafood, but this recipe changed my mind. Truly delicious!",
        edited=False,
        created_at=datetime(2023, 10, 17, 8, 15),
        updated_at=datetime(2023, 10, 17, 8, 15),
        review_likes=[user3, user6, user11],
    )

    review49 = Review(
        user_id=11,
        recipe_id=16,
        body="The seafood medley in this dish is perfectly cooked. It's a delightful culinary experience.",
        edited=True,
        created_at=datetime(2023, 10, 18, 12, 0),
        updated_at=datetime(2023, 10, 18, 13, 0),
        review_likes=[user1, user4, user9],
    )

    review50 = Review(
        user_id=12,
        recipe_id=17,
        body="This vegetarian dish is a delightful option for those looking for a tasty meatless meal.",
        edited=False,
        created_at=datetime(2023, 10, 19, 17, 30),
        updated_at=datetime(2023, 10, 19, 17, 30),
        review_likes=[user2, user5, user8],
    )

    review51 = Review(
        user_id=13,
        recipe_id=17,
        body="I'm always on the lookout for great vegetarian recipes, and this one is now a favorite of mine.",
        edited=True,
        created_at=datetime(2023, 10, 20, 14, 45),
        updated_at=datetime(2023, 10, 20, 15, 15),
        review_likes=[user3, user6, user9],
    )

    review52 = Review(
        user_id=1,
        recipe_id=17,
        body="The use of fresh vegetables in this recipe adds a wonderful crunch and flavor. Highly recommended!",
        edited=False,
        created_at=datetime(2023, 10, 21, 9, 15),
        updated_at=datetime(2023, 10, 21, 9, 15),
        review_likes=[user1, user4, user10],
    )

    review53 = Review(
        user_id=2,
        recipe_id=17,
        body="Even for non-vegetarians, this dish is a winner. The blend of spices is perfection.",
        edited=True,
        created_at=datetime(2023, 10, 22, 14, 0),
        updated_at=datetime(2023, 10, 22, 15, 0),
        review_likes=[user2, user7, user11],
    )

    review54 = Review(
        user_id=3,
        recipe_id=18,
        body="The aroma of this dish alone is enough to make your mouth water. A truly satisfying meal.",
        edited=False,
        created_at=datetime(2023, 10, 23, 18, 30),
        updated_at=datetime(2023, 10, 23, 18, 30),
        review_likes=[user1, user5, user8],
    )

    review55 = Review(
        user_id=4,
        recipe_id=18,
        body="The blend of spices and herbs in this recipe is masterful. A culinary journey for the taste buds.",
        edited=True,
        created_at=datetime(2023, 10, 24, 15, 45),
        updated_at=datetime(2023, 10, 24, 16, 15),
        review_likes=[user3, user6, user9],
    )

    review56 = Review(
        user_id=5,
        recipe_id=18,
        body="I've tried various versions of this dish, and this recipe stands out with its unique and bold flavors.",
        edited=False,
        created_at=datetime(2023, 10, 25, 10, 15),
        updated_at=datetime(2023, 10, 25, 10, 15),
        review_likes=[user2, user4, user10],
    )

    review57 = Review(
        user_id=6,
        recipe_id=18,
        body="This dish is perfect for spice enthusiasts. The heat level is just right, and the taste is exceptional.",
        edited=True,
        created_at=datetime(2023, 10, 26, 14, 0),
        updated_at=datetime(2023, 10, 26, 15, 0),
        review_likes=[user1, user7, user11],
    )
    review58 = Review(
        user_id=7,
        recipe_id=19,
        body="As a seafood lover, this recipe exceeded my expectations. The flavors are truly outstanding.",
        edited=False,
        created_at=datetime(2023, 10, 27, 18, 30),
        updated_at=datetime(2023, 10, 27, 18, 30),
        review_likes=[user2, user5, user8],
    )

    review59 = Review(
        user_id=8,
        recipe_id=19,
        body="This seafood dish is a work of art. The combination of ingredients creates a symphony of taste.",
        edited=True,
        created_at=datetime(2023, 10, 28, 15, 45),
        updated_at=datetime(2023, 10, 28, 16, 15),
        review_likes=[user3, user6, user9],
    )

    review60 = Review(
        user_id=9,
        recipe_id=19,
        body="I usually don't go for seafood, but this dish has converted me. Absolutely delicious!",
        edited=False,
        created_at=datetime(2023, 10, 29, 10, 15),
        updated_at=datetime(2023, 10, 29, 10, 15),
        review_likes=[user1, user4, user10],
    )

    review61 = Review(
        user_id=10,
        recipe_id=19,
        body="The seafood is perfectly cooked, and the accompanying sauce adds a delightful complexity.",
        edited=True,
        created_at=datetime(2023, 10, 30, 14, 0),
        updated_at=datetime(2023, 10, 30, 15, 0),
        review_likes=[user2, user7, user11],
    )

    review62 = Review(
        user_id=11,
        recipe_id=20,
        body="The combination of flavors in this dish is simply magical. A must-try for any food enthusiast.",
        edited=False,
        created_at=datetime(2023, 11, 1, 18, 30),
        updated_at=datetime(2023, 11, 1, 18, 30),
        review_likes=[user1, user5, user8],
    )

    review63 = Review(
        user_id=12,
        recipe_id=20,
        body="I'm not a fan of snacks, but this recipe changed my perspective. The crunchiness is addicting!",
        edited=True,
        created_at=datetime(2023, 11, 2, 15, 45),
        updated_at=datetime(2023, 11, 2, 16, 15),
        review_likes=[user3, user6, user9],
    )

    review64 = Review(
        user_id=13,
        recipe_id=20,
        body="This snack is perfect for movie nights. The mix of textures and flavors is a winning combination.",
        edited=False,
        created_at=datetime(2023, 11, 3, 10, 15),
        updated_at=datetime(2023, 11, 3, 10, 15),
        review_likes=[user1, user4, user10],
    )

    review65 = Review(
        user_id=1,
        recipe_id=20,
        body="An easy-to-make snack that doesn't compromise on taste. Great for quick cravings!",
        edited=True,
        created_at=datetime(2023, 11, 4, 14, 0),
        updated_at=datetime(2023, 11, 4, 15, 0),
        review_likes=[user2, user7, user11],
    )

    review66 = Review(
        user_id=2,
        recipe_id=21,
        body="A delightful vegetarian dish that even non-vegetarians will enjoy. The flavors are incredible.",
        edited=False,
        created_at=datetime(2023, 11, 5, 18, 30),
        updated_at=datetime(2023, 11, 5, 18, 30),
        review_likes=[user3, user6, user9],
    )

    review67 = Review(
        user_id=3,
        recipe_id=21,
        body="I appreciate the balance of flavors in this recipe. The combination of ingredients is spot-on.",
        edited=True,
        created_at=datetime(2023, 11, 6, 15, 45),
        updated_at=datetime(2023, 11, 6, 16, 15),
        review_likes=[user1, user4, user10],
    )

    review68 = Review(
        user_id=4,
        recipe_id=21,
        body="This recipe is a winner! It's hearty, flavorful, and perfect for a cozy dinner.",
        edited=False,
        created_at=datetime(2023, 11, 7, 10, 15),
        updated_at=datetime(2023, 11, 7, 10, 15),
        review_likes=[user2, user7, user11],
    )

    review69 = Review(
        user_id=5,
        recipe_id=21,
        body="I'm not a vegetarian, but I'd choose this dish any day. It's that good!",
        edited=True,
        created_at=datetime(2023, 11, 8, 14, 0),
        updated_at=datetime(2023, 11, 8, 15, 0),
        review_likes=[user8, user12, user13],
    )

    review70 = Review(
        user_id=6,
        recipe_id=22,
        body="This seafood dish is a masterpiece. The freshness of the ingredients shines through.",
        edited=False,
        created_at=datetime(2023, 11, 9, 18, 30),
        updated_at=datetime(2023, 11, 9, 18, 30),
        review_likes=[user1, user5, user9],
    )

    review71 = Review(
        user_id=7,
        recipe_id=22,
        body="The combination of flavors in this dish is exquisite. Definitely a restaurant-quality recipe!",
        edited=True,
        created_at=datetime(2023, 11, 10, 15, 45),
        updated_at=datetime(2023, 11, 10, 16, 15),
        review_likes=[user2, user6, user10],
    )

    review72 = Review(
        user_id=8,
        recipe_id=22,
        body="As a seafood lover, I can confidently say that this dish is one of the best I've ever had.",
        edited=False,
        created_at=datetime(2023, 11, 11, 10, 15),
        updated_at=datetime(2023, 11, 11, 10, 15),
        review_likes=[user3, user7, user11],
    )

    review73 = Review(
        user_id=9,
        recipe_id=22,
        body="This recipe has become a family favorite. The flavors are rich, and the preparation is straightforward.",
        edited=True,
        created_at=datetime(2023, 11, 12, 14, 0),
        updated_at=datetime(2023, 11, 12, 15, 0),
        review_likes=[user4, user8, user12],
    )



    reviews = [
        review1, review2, review3, review4, review5,
        review6, review7, review8, review9, review10,
        review11, review12, review13, review14, review15,
        review16, review17, review18, review19, review20,
        review21, review22, review23, review24, review25,
        review26, review27, review28, review29, review30,
        review31, review32, review33, review34, review35,
        review36, review37, review38, review39, review40,
        review41, review42, review43, review44, review45,
        review46, review47, review48, review49, review50,
        review51, review52, review53, review54, review55,
        review56, review57, review58, review59, review60,
        review61, review62, review63, review64, review65,
        review66, review67, review68, review69, review70,
        review71, review72, review73, review74, reivew75,
        review76, review77, reivew78, review79, review80,
        review81, review82, review83, review84, review85,
        review86, review87, review88, review89, review90,
        review91, review92, review93, review94, review95,
        review96, review97, review98, review99, review100,
        

        ]
    [db.session.add(review) for review in reviews]
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
