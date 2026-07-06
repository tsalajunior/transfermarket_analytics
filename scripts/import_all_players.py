from app.core.database import SessionLocal

from app.models.club import Club

from app.repositories.player_repository import PlayerRepository

from app.scraper.players_scraper import PlayerScraper


db = SessionLocal()

try:

    scraper = PlayerScraper()
    player_repo = PlayerRepository(db)

    clubs = db.query(Club).all()

    print(f"{len(clubs)} clubs trouvés")

    for club in clubs:

        print(f"\n=== {club.name} ===")

        players = scraper.get_players(club.url)

        print(f"{len(players)} joueurs trouvés")

        for player_data in players:

            player_repo.create_if_not_exists(
                tm_id=player_data["tm_id"],
                name=player_data["name"],
                nationality=player_data["nationality"],
                position=player_data["position"],
                market_value_eur=player_data["market_value"],
                url=player_data["url"],
                club_id=club.id
            )

            print(f"Import : {player_data['name']}")

finally:

    db.close()