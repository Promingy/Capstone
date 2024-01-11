from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

users = [
    User(
        first_name='Demo',
        last_name = 'lition',
        bio="My name is Demo-Lition and I'm really exicited to try new foods",
        email='demo@aa.io',
        password='password',
        profile_pic = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        ),
    User(
        first_name='marnie',
        last_name = 'tester',
        bio="I'm Marnie and I'd love to have a good tasting meal",
        email='marnie@aa.io',
        password='password',
        profile_pic = "https://i.pinimg.com/474x/dd/94/3d/dd943d14b334896b33a8d3ba8e0cde05.jpg"
        ),
    User(
        first_name='bobbie',
        last_name = 'builder',
        bio=" I'm Bob the Builder and I can always go for a good snack",
        email='bobbie@aa.io',
        password='password',
        profile_pic = "https://avatars.githubusercontent.com/u/5268568?v=4"
        )
]
# Adds a demo user, you can add other users here if you want
def seed_users():

    [db.session.add(user) for user in users]

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
