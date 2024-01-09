from app.models import db, Rating, environment, SCHEMA
from sqlalchemy.sql import text

def seed_ratings():
    """
    generates seed data for recipe ratings
    """

    rating1 = Rating(

    )
    rating1 = Rating(
        user_id=1,
        recipe_id=1,
        rating=1
    )
    rating2 = Rating(
        user_id=2,
        recipe_id=2,
        rating=3
    )
    rating3 = Rating(
        user_id=3,
        recipe_id=3,
        rating=4
    )
    rating4 = Rating(
        user_id=2,
        recipe_id=4,
        rating=5
    )
    rating5 = Rating(
        user_id=1,
        recipe_id=5,
        rating=2
    )

    ratings = [rating1, rating2, rating3, rating4, rating5]

    [db.session.add(rating) for rating in ratings]
    db.session.commit()

def undo_ratings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ratings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ratings"))

    db.session.commit()
