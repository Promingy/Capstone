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
        ),
    User(
        first_name="John",
        last_name="Doe",
        bio="Food lover and enthusiast",
        email="john.doe@email.com",
        password="password",
        profile_pic="https://media.istockphoto.com/id/1300512215/photo/headshot-portrait-of-smiling-ethnic-businessman-in-office.jpg?s=612x612&w=0&k=20&c=QjebAlXBgee05B3rcLDAtOaMtmdLjtZ5Yg9IJoiy-VY="
    ),
    User(
        first_name="Jane",
        last_name="Smith",
        bio="Passionate about cooking and baking",
        email="jane.smith@email.com",
        password="password",
        profile_pic="https://t3.ftcdn.net/jpg/03/67/46/48/360_F_367464887_f0w1JrL8PddfuH3P2jSPlIGjKU2BI0rn.jpg"
    ),
    User(
        first_name="David",
        last_name="Williams",
        bio="Exploring the world of flavors",
        email="david.williams@email.com",
        password="password",
        profile_pic="https://media.istockphoto.com/id/1388253782/photo/positive-successful-millennial-business-professional-man-head-shot-portrait.jpg?s=612x612&w=0&k=20&c=uS4knmZ88zNA_OjNaE_JCRuq9qn3ycgtHKDKdJSnGdY="
    ),
    User(
        first_name="Emma",
        last_name="Johnson",
        bio="Foodie on a culinary journey",
        email="emma.johnson@email.com",
        password="password",
        profile_pic="https://images.pexels.com/photos/3763188/pexels-photo-3763188.jpeg?cs=srgb&dl=pexels-andrea-piacquadio-3763188.jpg&fm=jpg"
    ),
    User(
        first_name="Michael",
        last_name="Brown",
        bio="Adventurous eater and chef",
        email="michael.brown@email.com",
        password="password",
        profile_pic="https://img.freepik.com/free-photo/portrait-young-asian-man-looking-confident-taking-selfie-while-standing-outdoors-street_58466-11951.jpg"
    ),
    User(
        first_name="Emily",
        last_name="Taylor",
        bio="Cooking is my therapy",
        email="emily.taylor@email.com",
        password="password",
        profile_pic="https://img.freepik.com/free-photo/portrait-young-asian-man-looking-confident-taking-selfie-while-standing-outdoors-street_58466-11951.jpg"
    ),
    User(
        first_name="Dylan",
        last_name="Miller",
        bio="Creating culinary masterpieces",
        email="dylan.miller@email.com",
        password="password",
        profile_pic="https://www.stockvault.net//data/2009/06/09/109080/thumb16.jpg"
    ),
    User(
        first_name="Sophia",
        last_name="Davis",
        bio="Food brings people together",
        email="sophia.davis@email.com",
        password="password",
        profile_pic="https://t3.ftcdn.net/jpg/03/95/11/56/360_F_395115694_a2GXhquKxSllHdix4cv1UOKYd4hGoBTF.jpg"
    ),
    User(
        first_name="Mason",
        last_name="Wilson",
        bio="Food explorer and creator",
        email="mason.wilson@email.com",
        password="password",
        profile_pic="https://healthprofessions.ucf.edu/wp-content/uploads/sites/2/2018/06/Matt-Stock.jpg"
    ),
    User(
        first_name="Ava",
        last_name="Jones",
        bio="Passionate about healthy living",
        email="ava.jones@email.com",
        password="password",
        profile_pic="https://www.shutterstock.com/image-photo/young-beautiful-brunette-woman-wearing-600nw-1667900191.jpg"
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
