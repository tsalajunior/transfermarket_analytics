from datetime import date


def calculate_age(birth_date):
    """
    Calcule l'âge d'une personne à partir de sa date de naissance.

    Args:
        birth_date (date | None)

    Returns:
        int | None
    """

    if birth_date is None:
        return None

    today = date.today()

    age = (
        today.year
        - birth_date.year
        - (
            (today.month, today.day)
            < (birth_date.month, birth_date.day)
        )
    )

    return age