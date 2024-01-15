from app.models import db, Category, environment, SCHEMA
from sqlalchemy.sql import text

def seed_categories ():
    category1 = Category(id=1, category="Appetizer")
    category2 = Category(id=2, category="Main Course")
    category3 = Category(id=3, category="Dessert")
    category4 = Category(id=4, category="Salad")
    category5 = Category(id=5, category="Soup")
    category6 = Category(id=6, category="Beverage")
    category7 = Category(id=7, category="Vegetarian")
    category8 = Category(id=8, category="Seafood")
    category9 = Category(id=9, category="Pasta")
    category10 = Category(id=10, category="Snack")

    categories = [category1, category2, category3, category4, category5, category6, category7, category8, category9, category10]

    [db.session.add(category) for category in categories]
    db.session.commit()

def unseed_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM categories"))

    db.session.commit()
