from datetime import date

from app.utils.date_utils import calculate_age


def test_calculate_age():
    birth_date = date(2000, 1, 1)

    age = calculate_age(birth_date)

    assert age >= 25