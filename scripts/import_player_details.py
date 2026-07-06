from datetime import datetime

from app.core.database import SessionLocal
from app.models.player import Player
from app.scraper.player_profile_scraper import PlayerProfileScraper


db = SessionLocal()

scraper = PlayerProfileScraper()

players = db.query(Player).all()

print(f"{len(players)} joueurs trouvés\n")

for player in players:

    try:

        if not player.url:
            print(f"URL manquante : {player.name}")
            continue

        print(f"Scraping : {player.name}")

        details = scraper.get_player_details(
            player.url
        )

        # Date de naissance
        if details["birth_date"]:

            player.birth_date = datetime.strptime(
                details["birth_date"],
                "%d/%m/%Y"
            ).date()

        # Taille
        if details["height_cm"]:

            player.height_cm = details["height_cm"]

        # Pied fort
        if details["foot"]:

            player.foot = details["foot"]

        db.commit()

        print(
            f"OK | "
            f"Naissance={player.birth_date} | "
            f"Taille={player.height_cm} | "
            f"Pied={player.foot}"
        )

    except Exception as e:

        db.rollback()

        print(
            f"Erreur {player.name} : {e}"
        )

print("\nImport terminé.")