from app.models import db, Rating, environment, SCHEMA
from sqlalchemy.sql import text

def seed_ratings():
    """
    generates seed data for recipe ratings
    """

    rating1 = Rating(user_id=1, recipe_id=1, rating=4)
    rating2 = Rating(user_id=2, recipe_id=1, rating=3)
    rating3 = Rating(user_id=3, recipe_id=1, rating=5)
    rating109 = Rating(user_id=4, recipe_id=1, rating=2)
    rating110 = Rating(user_id=5, recipe_id=1, rating=4)

    rating4 = Rating(user_id=4, recipe_id=2, rating=5)
    rating5 = Rating(user_id=5, recipe_id=2, rating=4)
    rating6 = Rating(user_id=6, recipe_id=2, rating=3)
    rating112 = Rating(user_id=7, recipe_id=2, rating=4)
    rating113 = Rating(user_id=8, recipe_id=2, rating=3)
    rating114 = Rating(user_id=9, recipe_id=2, rating=5)

    rating7 = Rating(user_id=7, recipe_id=3, rating=5)
    rating8 = Rating(user_id=8, recipe_id=3, rating=4)
    rating9 = Rating(user_id=9, recipe_id=3, rating=3)
    rating115 = Rating(user_id=10, recipe_id=3, rating=2)
    rating116 = Rating(user_id=11, recipe_id=3, rating=4)
    rating117 = Rating(user_id=12, recipe_id=3, rating=5)
    rating118 = Rating(user_id=13, recipe_id=3, rating=3)

    rating119 = Rating(user_id=1, recipe_id=4, rating=4)
    rating120 = Rating(user_id=2, recipe_id=4, rating=5)
    rating121 = Rating(user_id=3, recipe_id=4, rating=3)
    rating10 = Rating(user_id=10, recipe_id=4, rating=5)
    rating11 = Rating(user_id=11, recipe_id=4, rating=4)
    rating12 = Rating(user_id=12, recipe_id=4, rating=3)

    rating13 = Rating(user_id=1, recipe_id=5, rating=5)
    rating14 = Rating(user_id=2, recipe_id=5, rating=4)
    rating15 = Rating(user_id=3, recipe_id=5, rating=3)
    rating122 = Rating(user_id=4, recipe_id=5, rating=2)
    rating123 = Rating(user_id=5, recipe_id=5, rating=4)
    rating124 = Rating(user_id=6, recipe_id=5, rating=5)
    rating125 = Rating(user_id=7, recipe_id=5, rating=3)

    rating16 = Rating(user_id=4, recipe_id=6, rating=5)
    rating17 = Rating(user_id=5, recipe_id=6, rating=4)
    rating18 = Rating(user_id=6, recipe_id=6, rating=3)
    rating126 = Rating(user_id=8, recipe_id=6, rating=5)
    rating127 = Rating(user_id=9, recipe_id=6, rating=4)

    rating19 = Rating(user_id=7, recipe_id=7, rating=5)
    rating20 = Rating(user_id=8, recipe_id=7, rating=4)
    rating21 = Rating(user_id=9, recipe_id=7, rating=3)
    rating128 = Rating(user_id=10, recipe_id=7, rating=3)
    rating129 = Rating(user_id=11, recipe_id=7, rating=5)
    rating130 = Rating(user_id=12, recipe_id=7, rating=4)

    rating23 = Rating(user_id=1, recipe_id=8, rating=4)
    rating24 = Rating(user_id=2, recipe_id=8, rating=3)
    rating22 = Rating(user_id=10, recipe_id=8, rating=5)
    rating131 = Rating(user_id=13, recipe_id=8, rating=5)

    rating132 = Rating(user_id=1, recipe_id=9, rating=4)
    rating133 = Rating(user_id=2, recipe_id=9, rating=3)
    rating134 = Rating(user_id=3, recipe_id=9, rating=5)
    rating26 = Rating(user_id=4, recipe_id=9, rating=4)
    rating27 = Rating(user_id=5, recipe_id=9, rating=3)

    rating135 = Rating(user_id=4, recipe_id=10, rating=2)
    rating136 = Rating(user_id=5, recipe_id=10, rating=4)
    rating137 = Rating(user_id=6, recipe_id=10, rating=5)
    rating138 = Rating(user_id=7, recipe_id=10, rating=3)
    rating30 = Rating(user_id=8, recipe_id=10, rating=3)

    rating139 = Rating(user_id=8, recipe_id=11, rating=5)
    rating140 = Rating(user_id=9, recipe_id=11, rating=4)
    rating32 = Rating(user_id=10, recipe_id=11, rating=4)
    rating33 = Rating(user_id=11, recipe_id=11, rating=3)

    rating35 = Rating(user_id=1, recipe_id=12, rating=4)
    rating36 = Rating(user_id=2, recipe_id=12, rating=3)
    rating141 = Rating(user_id=10, recipe_id=12, rating=3)
    rating142 = Rating(user_id=11, recipe_id=12, rating=5)
    rating143 = Rating(user_id=12, recipe_id=12, rating=4)

    rating37 = Rating(user_id=3, recipe_id=13, rating=5)
    rating38 = Rating(user_id=4, recipe_id=13, rating=4)
    rating39 = Rating(user_id=5, recipe_id=13, rating=3)
    rating144 = Rating(user_id=13, recipe_id=13, rating=2)

    rating145 = Rating(user_id=1, recipe_id=14, rating=4)
    rating146 = Rating(user_id=2, recipe_id=14, rating=5)
    rating147 = Rating(user_id=3, recipe_id=14, rating=3)
    rating40 = Rating(user_id=6, recipe_id=14, rating=5)
    rating41 = Rating(user_id=7, recipe_id=14, rating=4)
    rating42 = Rating(user_id=8, recipe_id=14, rating=3)

    rating148 = Rating(user_id=4, recipe_id=15, rating=2)
    rating149 = Rating(user_id=5, recipe_id=15, rating=4)
    rating150 = Rating(user_id=6, recipe_id=15, rating=5)
    rating43 = Rating(user_id=9, recipe_id=15, rating=5)
    rating44 = Rating(user_id=10, recipe_id=15, rating=4)
    rating45 = Rating(user_id=11, recipe_id=15, rating=3)

    rating47 = Rating(user_id=1, recipe_id=16, rating=4)
    rating48 = Rating(user_id=2, recipe_id=16, rating=3)
    rating151 = Rating(user_id=7, recipe_id=16, rating=3)
    rating152 = Rating(user_id=8, recipe_id=16, rating=5)
    rating46 = Rating(user_id=12, recipe_id=16, rating=5)

    rating49 = Rating(user_id=3, recipe_id=17, rating=5)
    rating50 = Rating(user_id=4, recipe_id=17, rating=4)
    rating51 = Rating(user_id=5, recipe_id=17, rating=3)
    rating153 = Rating(user_id=9, recipe_id=17, rating=4)

    rating52 = Rating(user_id=6, recipe_id=18, rating=5)
    rating53 = Rating(user_id=7, recipe_id=18, rating=4)
    rating54 = Rating(user_id=8, recipe_id=18, rating=3)
    rating154 = Rating(user_id=10, recipe_id=18, rating=3)
    rating155 = Rating(user_id=11, recipe_id=18, rating=5)
    rating156 = Rating(user_id=12, recipe_id=18, rating=4)

    rating55 = Rating(user_id=9, recipe_id=19, rating=5)
    rating56 = Rating(user_id=10, recipe_id=19, rating=4)
    rating57 = Rating(user_id=11, recipe_id=19, rating=3)
    rating157 = Rating(user_id=13, recipe_id=19, rating=2)

    rating59 = Rating(user_id=1, recipe_id=20, rating=4)
    rating60 = Rating(user_id=2, recipe_id=20, rating=3)
    rating160 = Rating(user_id=3, recipe_id=20, rating=3)
    rating58 = Rating(user_id=12, recipe_id=20, rating=5)

    rating61 = Rating(user_id=3, recipe_id=21, rating=5)
    rating161 = Rating(user_id=4, recipe_id=21, rating=2)
    rating63 = Rating(user_id=5, recipe_id=21, rating=3)
    rating163 = Rating(user_id=6, recipe_id=21, rating=5)

    rating64 = Rating(user_id=6, recipe_id=22, rating=5)
    rating164 = Rating(user_id=7, recipe_id=22, rating=3)
    rating66 = Rating(user_id=8, recipe_id=22, rating=3)

    rating166 = Rating(user_id=9, recipe_id=23, rating=4)
    rating68 = Rating(user_id=10, recipe_id=23, rating=4)
    rating69 = Rating(user_id=11, recipe_id=23, rating=3)

    rating71 = Rating(user_id=1, recipe_id=24, rating=4)
    rating72 = Rating(user_id=2, recipe_id=24, rating=3)
    rating167 = Rating(user_id=10, recipe_id=24, rating=3)
    rating168 = Rating(user_id=11, recipe_id=24, rating=5)
    rating169 = Rating(user_id=12, recipe_id=24, rating=4)

    rating73 = Rating(user_id=3, recipe_id=25, rating=5)
    rating74 = Rating(user_id=4, recipe_id=25, rating=4)
    rating75 = Rating(user_id=5, recipe_id=25, rating=3)
    rating170 = Rating(user_id=13, recipe_id=25, rating=2)

    rating171 = Rating(user_id=1, recipe_id=26, rating=4)
    rating172 = Rating(user_id=2, recipe_id=26, rating=5)
    rating173 = Rating(user_id=3, recipe_id=26, rating=3)
    rating76 = Rating(user_id=6, recipe_id=26, rating=5)
    rating77 = Rating(user_id=7, recipe_id=26, rating=4)
    rating78 = Rating(user_id=8, recipe_id=26, rating=3)

    rating174 = Rating(user_id=4, recipe_id=27, rating=2)
    rating175 = Rating(user_id=5, recipe_id=27, rating=4)
    rating176 = Rating(user_id=6, recipe_id=27, rating=5)
    rating79 = Rating(user_id=9, recipe_id=27, rating=5)
    rating80 = Rating(user_id=10, recipe_id=27, rating=4)
    rating81 = Rating(user_id=11, recipe_id=27, rating=3)

    rating83 = Rating(user_id=1, recipe_id=28, rating=4)
    rating84 = Rating(user_id=2, recipe_id=28, rating=3)
    rating177 = Rating(user_id=7, recipe_id=28, rating=3)
    rating178 = Rating(user_id=8, recipe_id=28, rating=5)
    rating82 = Rating(user_id=12, recipe_id=28, rating=5)

    rating85 = Rating(user_id=3, recipe_id=29, rating=5)
    rating86 = Rating(user_id=4, recipe_id=29, rating=4)
    rating87 = Rating(user_id=5, recipe_id=29, rating=3)
    rating179 = Rating(user_id=9, recipe_id=29, rating=4)

    rating88 = Rating(user_id=6, recipe_id=30, rating=5)
    rating89 = Rating(user_id=7, recipe_id=30, rating=4)
    rating90 = Rating(user_id=8, recipe_id=30, rating=3)
    rating180 = Rating(user_id=10, recipe_id=30, rating=3)
    rating181 = Rating(user_id=11, recipe_id=30, rating=5)
    rating182 = Rating(user_id=12, recipe_id=30, rating=4)

    rating91 = Rating(user_id=9, recipe_id=31, rating=5)
    rating92 = Rating(user_id=10, recipe_id=31, rating=4)
    rating93 = Rating(user_id=11, recipe_id=31, rating=3)
    rating183 = Rating(user_id=13, recipe_id=31, rating=2)

    rating184 = Rating(user_id=1, recipe_id=32, rating=4)
    rating96 = Rating(user_id=2, recipe_id=32, rating=3)
    rating186 = Rating(user_id=3, recipe_id=32, rating=3)
    rating94 = Rating(user_id=12, recipe_id=32, rating=5)

    rating187 = Rating(user_id=4, recipe_id=33, rating=2)
    rating97 = Rating(user_id=3, recipe_id=33, rating=5)
    rating99 = Rating(user_id=5, recipe_id=33, rating=3)
    rating189 = Rating(user_id=6, recipe_id=33, rating=5)

    rating100 = Rating(user_id=6, recipe_id=34, rating=5)
    rating101 = Rating(user_id=7, recipe_id=34, rating=4)
    rating102 = Rating(user_id=8, recipe_id=34, rating=3)

    rating192 = Rating(user_id=9, recipe_id=35, rating=4)
    rating104 = Rating(user_id=10, recipe_id=35, rating=4)
    rating105 = Rating(user_id=11, recipe_id=35, rating=3)


    ratings = [
        rating1, rating2, rating3, rating4, rating5,
        rating6, rating7, rating8, rating9, rating10,
        rating11, rating12, rating13, rating14, rating15,
        rating16, rating17, rating18, rating19, rating20,
        rating21, rating22, rating23, rating24, rating26,
        rating27, rating30, rating32, rating33, rating35,
        rating36, rating37, rating38, rating39, rating40,
        rating41, rating42, rating43, rating44, rating45,
        rating46, rating47, rating48, rating49, rating50,
        rating51, rating52, rating53, rating54, rating55,
        rating56, rating57, rating58, rating59, rating60,
        rating61, rating63, rating64, rating66, rating68,
        rating69, rating71, rating72, rating73, rating74,
        rating75, rating76, rating77, rating78, rating79,
        rating80, rating81, rating82, rating83, rating84,
        rating85, rating86, rating87, rating88, rating89,
        rating90, rating91, rating92, rating93, rating94,
        rating96, rating97, rating99, rating100, rating101,
        rating102, rating104, rating105, rating109, rating110,
        rating112, rating113, rating114, rating115, rating116,
        rating117, rating118, rating119, rating120, rating121,
        rating122, rating123, rating124, rating125, rating126,
        rating127, rating128, rating129, rating130, rating131,
        rating132, rating133, rating134, rating135, rating136,
        rating137, rating138, rating139, rating140, rating141,
        rating142, rating143, rating144, rating145, rating146,
        rating149, rating148, rating149, rating150, rating151,
        rating152, rating153, rating154, rating155, rating156,
        rating157, rating160, rating161, rating163, rating164,
        rating166, rating167, rating168, rating169, rating170,
        rating171, rating172, rating173, rating174, rating175,
        rating176, rating177, rating178, rating179, rating180,
        rating181, rating182, rating183, rating184, rating186,
        rating187, rating189, rating192
    ]


    [db.session.add(rating) for rating in ratings]
    db.session.commit()

def undo_ratings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ratings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ratings"))

    db.session.commit()
