from flask import Blueprint
from ..models import Measurement, Category

dropdown = Blueprint('dropdowns', __name__)

@dropdown.route('')
def get_dropdown_items():
    categories = [category.to_dict() for category in Category.query.all()]
    measurements = [measurement.to_dict() for measurement in Measurement.query.all()]

    return {"categories": categories, "measurements": measurements}
