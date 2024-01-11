from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime
from .users import users

user1, user2, user3 = users

def seed_reviews() :
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

    reviews = [ review1, review2, review3, review4, review5]
    [db.session.add(review) for review in reviews]
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
