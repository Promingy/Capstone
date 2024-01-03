from flask import Blueprint

recipe = Blueprint('recipes', __name__)

@recipe.route('/')
def get_all_recipes():
    return {"test" : "test"}
