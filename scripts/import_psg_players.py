from app.core.database import SessionLocal

from app.scraper.players_scraper import PlayerScraper

from app.repositories.club_repository import ClubRepository
from app.repositories.player_repository import PlayerRepository


db = SessionLocal()

try:

    club_repo = ClubRepository(db)
    player_repo = PlayerRepository(db)

    psg = club_repo.get_by_tm_id("583")

    if not psg:
        raise Exception("PSG introuvable")

    scraper = PlayerScraper()

    players = scraper.get_players("/fc-paris-saint-germain/startseite/verein/583")

    print(f"{len(players)} joueurs récupérés")

    for player_data in players:

        player_repo.create_if_not_exists(
            tm_id=player_data["tm_id"],
            name=player_data["name"],
            nationality=player_data["nationality"],
            position=player_data["position"],
            market_value_eur=player_data["market_value"],
            club_id=psg.id
        )

        print("Import :", player_data["name"])

finally:
    db.close()