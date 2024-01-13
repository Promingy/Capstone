from app.models import db, Rating, environment, SCHEMA
from sqlalchemy.sql import text

def seed_ratings():
    """
    generates seed data for recipe ratings
    """

    rating1 = Rating(user_id=1, recipe_id=1, rating=4)
    rating2 = Rating(user_id=2, recipe_id=1, rating=3)
    rating3 = Rating(user_id=3, recipe_id=1, rating=5)
    rating4 = Rating(user_id=4, recipe_id=2, rating=5)
    rating5 = Rating(user_id=5, recipe_id=2, rating=4)
    rating6 = Rating(user_id=6, recipe_id=2, rating=3)
    rating7 = Rating(user_id=7, recipe_id=3, rating=5)
    rating8 = Rating(user_id=8, recipe_id=3, rating=4)
    rating9 = Rating(user_id=9, recipe_id=3, rating=3)
    rating10 = Rating(user_id=10, recipe_id=4, rating=5)
    rating11 = Rating(user_id=11, recipe_id=4, rating=4)
    rating12 = Rating(user_id=12, recipe_id=4, rating=3)
    rating13 = Rating(user_id=1, recipe_id=5, rating=5)
    rating14 = Rating(user_id=2, recipe_id=5, rating=4)
    rating15 = Rating(user_id=3, recipe_id=5, rating=3)
    rating16 = Rating(user_id=4, recipe_id=6, rating=5)
    rating17 = Rating(user_id=5, recipe_id=6, rating=4)
    rating18 = Rating(user_id=6, recipe_id=6, rating=3)
    rating19 = Rating(user_id=7, recipe_id=7, rating=5)
    rating20 = Rating(user_id=8, recipe_id=7, rating=4)
    rating21 = Rating(user_id=9, recipe_id=7, rating=3)
    rating22 = Rating(user_id=10, recipe_id=8, rating=5)
    rating23 = Rating(user_id=1, recipe_id=8, rating=4)
    rating24 = Rating(user_id=2, recipe_id=8, rating=3)
    rating25 = Rating(user_id=3, recipe_id=9, rating=5)
    rating26 = Rating(user_id=4, recipe_id=9, rating=4)
    rating27 = Rating(user_id=5, recipe_id=9, rating=3)
    rating28 = Rating(user_id=6, recipe_id=10, rating=5)
    rating29 = Rating(user_id=7, recipe_id=10, rating=4)
    rating30 = Rating(user_id=8, recipe_id=10, rating=3)
    rating31 = Rating(user_id=9, recipe_id=11, rating=5)
    rating32 = Rating(user_id=10, recipe_id=11, rating=4)
    rating33 = Rating(user_id=11, recipe_id=11, rating=3)
    rating34 = Rating(user_id=12, recipe_id=12, rating=5)
    rating35 = Rating(user_id=1, recipe_id=12, rating=4)
    rating36 = Rating(user_id=2, recipe_id=12, rating=3)
    rating37 = Rating(user_id=3, recipe_id=13, rating=5)
    rating38 = Rating(user_id=4, recipe_id=13, rating=4)
    rating39 = Rating(user_id=5, recipe_id=13, rating=3)
    rating40 = Rating(user_id=6, recipe_id=14, rating=5)
    rating41 = Rating(user_id=7, recipe_id=14, rating=4)
    rating42 = Rating(user_id=8, recipe_id=14, rating=3)
    rating43 = Rating(user_id=9, recipe_id=15, rating=5)
    rating44 = Rating(user_id=10, recipe_id=15, rating=4)
    rating45 = Rating(user_id=11, recipe_id=15, rating=3)
    rating46 = Rating(user_id=12, recipe_id=16, rating=5)
    rating47 = Rating(user_id=1, recipe_id=16, rating=4)
    rating48 = Rating(user_id=2, recipe_id=16, rating=3)
    rating49 = Rating(user_id=3, recipe_id=17, rating=5)
    rating50 = Rating(user_id=4, recipe_id=17, rating=4)
    rating51 = Rating(user_id=5, recipe_id=17, rating=3)
    rating52 = Rating(user_id=6, recipe_id=18, rating=5)
    rating53 = Rating(user_id=7, recipe_id=18, rating=4)
    rating54 = Rating(user_id=8, recipe_id=18, rating=3)
    rating55 = Rating(user_id=9, recipe_id=19, rating=5)
    rating56 = Rating(user_id=10, recipe_id=19, rating=4)
    rating57 = Rating(user_id=11, recipe_id=19, rating=3)
    rating58 = Rating(user_id=12, recipe_id=20, rating=5)
    rating59 = Rating(user_id=1, recipe_id=20, rating=4)
    rating60 = Rating(user_id=2, recipe_id=20, rating=3)
    rating61 = Rating(user_id=3, recipe_id=21, rating=5)
    rating62 = Rating(user_id=4, recipe_id=21, rating=4)
    rating63 = Rating(user_id=5, recipe_id=21, rating=3)
    rating64 = Rating(user_id=6, recipe_id=22, rating=5)
    rating65 = Rating(user_id=7, recipe_id=22, rating=4)
    rating66 = Rating(user_id=8, recipe_id=22, rating=3)
    rating67 = Rating(user_id=9, recipe_id=23, rating=5)
    rating68 = Rating(user_id=10, recipe_id=23, rating=4)
    rating69 = Rating(user_id=11, recipe_id=23, rating=3)
    rating70 = Rating(user_id=12, recipe_id=24, rating=5)
    rating71 = Rating(user_id=1, recipe_id=24, rating=4)
    rating72 = Rating(user_id=2, recipe_id=24, rating=3)
    rating73 = Rating(user_id=3, recipe_id=25, rating=5)
    rating74 = Rating(user_id=4, recipe_id=25, rating=4)
    rating75 = Rating(user_id=5, recipe_id=25, rating=3)
    rating76 = Rating(user_id=6, recipe_id=26, rating=5)
    rating77 = Rating(user_id=7, recipe_id=26, rating=4)
    rating78 = Rating(user_id=8, recipe_id=26, rating=3)
    rating79 = Rating(user_id=9, recipe_id=27, rating=5)
    rating80 = Rating(user_id=10, recipe_id=27, rating=4)
    rating81 = Rating(user_id=11, recipe_id=27, rating=3)
    rating82 = Rating(user_id=12, recipe_id=28, rating=5)
    rating83 = Rating(user_id=1, recipe_id=28, rating=4)
    rating84 = Rating(user_id=2, recipe_id=28, rating=3)
    rating85 = Rating(user_id=3, recipe_id=29, rating=5)
    rating86 = Rating(user_id=4, recipe_id=29, rating=4)
    rating87 = Rating(user_id=5, recipe_id=29, rating=3)
    rating88 = Rating(user_id=6, recipe_id=30, rating=5)
    rating89 = Rating(user_id=7, recipe_id=30, rating=4)
    rating90 = Rating(user_id=8, recipe_id=30, rating=3)
    rating91 = Rating(user_id=9, recipe_id=31, rating=5)
    rating92 = Rating(user_id=10, recipe_id=31, rating=4)
    rating93 = Rating(user_id=11, recipe_id=31, rating=3)
    rating94 = Rating(user_id=12, recipe_id=32, rating=5)
    rating95 = Rating(user_id=1, recipe_id=32, rating=4)
    rating96 = Rating(user_id=2, recipe_id=32, rating=3)
    rating97 = Rating(user_id=3, recipe_id=33, rating=5)
    rating98 = Rating(user_id=4, recipe_id=33, rating=4)
    rating99 = Rating(user_id=5, recipe_id=33, rating=3)
    rating100 = Rating(user_id=6, recipe_id=34, rating=5)
    rating101 = Rating(user_id=7, recipe_id=34, rating=4)
    rating102 = Rating(user_id=8, recipe_id=34, rating=3)
    rating103 = Rating(user_id=9, recipe_id=35, rating=5)
    rating104 = Rating(user_id=10, recipe_id=35, rating=4)
    rating105 = Rating(user_id=11, recipe_id=35, rating=3)

    ratings = [
        rating1, rating2, rating3, rating4, rating5,
        rating6, rating7, rating8, rating9, rating10,
        rating11, rating12, rating13, rating14, rating15,
        rating16, rating17, rating18, rating19, rating20,
        rating21, rating22, rating23, rating24, rating25,
        rating26, rating27, rating28, rating29, rating30,
        rating31, rating32, rating33, rating34, rating35,
        rating36, rating37, rating38, rating39, rating40,
        rating41, rating42, rating43, rating44, rating45,
        rating46, rating47, rating48, rating49, rating50,
        rating51, rating52, rating53, rating54, rating55,
        rating56, rating57, rating58, rating59, rating60,
        rating61, rating62, rating63, rating64, rating65,
        rating66, rating67, rating68, rating69, rating70,
        rating71, rating72, rating73, rating74, rating75,
        rating76, rating77, rating78, rating79, rating80,
        rating81, rating82, rating83, rating84, rating85,
        rating86, rating87, rating88, rating89, rating90,
        rating91, rating92, rating93, rating94, rating95,
        rating96, rating97, rating98, rating99, rating100,
        rating101, rating102, rating103, rating104, rating105
    ]


    [db.session.add(rating) for rating in ratings]
    db.session.commit()

def undo_ratings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ratings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ratings"))

    db.session.commit()
