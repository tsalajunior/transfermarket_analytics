from app.core.database import SessionLocal
from app.repositories.club_repository import ClubRepository
from app.repositories.league_repository import LeagueRepository
from app.scraper.league_scraper import LeagueScraper

db = SessionLocal()

club_repo = ClubRepository(db)
league_repo = LeagueRepository(db)

league = league_repo.get_by_tm_id("FR1")

scraper = LeagueScraper()

clubs = scraper.get_clubs(
    "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1"
)

print(f"{len(clubs)} clubs trouvés")

for club_data in clubs:

    club_repo.create_if_not_exists(
        tm_id=club_data["tm_id"],
        name=club_data["name"],
        url=club_data["url"],
        country="France",
        league_id=league.id
    )

    print("Import :", club_data["name"])

db.close()