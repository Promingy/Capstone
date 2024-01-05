from app.models import db, Measurement, environment, SCHEMA
from sqlalchemy.sql import text

def seed_measurements() :
    """
    Func that adds pre-seeded measurements to the database
    """

    floz = Measurement(
        measurement_name = "Fluid Ounce"
    )
    c = Measurement(
        measurement_name = "Cup"
    )
    pt = Measurement(
        measurement_name = "Pint"
    )
    qt = Measurement(
        measurement_name = "Quart"
    )
    gal = Measurement(
        measurement_name = "Gallon"
    )
    oz = Measurement(
        measurement_name = "Ounce"
    )
    lb = Measurement(
        measurement_name = "Pound"
    )
    g = Measurement(
        measurement_name = "Gram"
    )
    kg = Measurement(
        measurement_name = "Kilogram"
    )
    count = Measurement(
        measurement_name = "Count"
    )

    measurements = [floz, c, pt, qt, gal, oz, lb, g, kg, count]
    [db.session.add(measurement) for measurement in measurements]
    db.session.commit()

def undo_measurements() :
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.measurements RESTART IDENTITY CASCADE")

    else:
        db.session.execute(text('DELETE FROM measurements'))

    db.session.commit()
