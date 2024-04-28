from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

ViewedRecipe = db.Table(
    "viewedrecipes",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
    db.Column("recipe_id", db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), primary_key=True),
    db.Column("viewed_at", db.DateTime(timezone=True), default=func.now())
)

if environment == 'production':
    ViewedRecipe.schema = SCHEMA
