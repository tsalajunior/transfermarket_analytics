from app.core.database import SessionLocal

from app.repositories.league_repository import LeagueRepository


db = SessionLocal()

repo = LeagueRepository(db)

league = repo.create_if_not_exists(
    tm_id="FR1",
    name="Ligue 1",
    country="France",
    tier=1
)

print(
    league.id,
    league.tm_id,
    league.name
)

db.close()