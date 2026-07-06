from app.core.database import SessionLocal
from app.repositories.league_repository import LeagueRepository

db = SessionLocal()

repo = LeagueRepository(db)

for league in repo.get_all():
    print(league.name)