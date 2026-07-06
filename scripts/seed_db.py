from datetime import date

from app.core.database import SessionLocal

from app.models.league import League
from app.models.club import Club
from app.models.player import Player


db = SessionLocal()

try:

    # championnat
    ligue1 = League(
        tm_id="L1",
        name="Ligue 1",
        country="France",
        tier=1
    )

    db.add(ligue1)
    db.flush()

    # club
    psg = Club(
        tm_id="PSG001",
        name="Paris Saint-Germain",
        country="France",
        league_id=ligue1.id
    )

    db.add(psg)
    db.flush()

    # joueurs
    dembele = Player(
        tm_id="P001",
        name="Ousmane Dembélé",
        birth_date=date(1997, 5, 15),
        nationality="France",
        position="Right Winger",
        market_value_eur=90000000,
        club_id=psg.id
    )

    hakimi = Player(
        tm_id="P002",
        name="Achraf Hakimi",
        birth_date=date(1998, 11, 4),
        nationality="Morocco",
        position="Right Back",
        market_value_eur=70000000,
        club_id=psg.id
    )

    db.add_all([dembele, hakimi])

    db.commit()

    print("Données insérées avec succès")

except Exception as e:
    db.rollback()
    print("Erreur :", e)

finally:
    db.close()