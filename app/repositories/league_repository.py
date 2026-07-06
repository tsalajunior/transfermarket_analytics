from os import name

from sqlalchemy.orm import Session

from app.models.league import League
from app.models.stat import PlayerStat


class LeagueRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_tm_id(self, tm_id: str):
        return (
            self.db.query(League)
            .filter(League.tm_id == tm_id)
            .first()
        )
    def get_by_name(self, name: str):
        return (
            self.db.query(League)
            .filter(League.name == name)
            .first()
        )

    def create(self, league: League):
        self.db.add(league)
        self.db.commit()
        self.db.refresh(league)
        return league

    def get_all(self):
        return self.db.query(League).all()
    
    def create_if_not_exists(self, tm_id: str, name: str, country: str, tier: int):
        league = self.get_by_tm_id(tm_id)

        if league:
            return league

        league = League(
            tm_id=tm_id,
            name=name,
            country=country,
            tier=tier
        )

        self.db.add(league)
        self.db.commit()
        self.db.refresh(league)

        return league
    
    def get_seasons(self):

        return (
            self.db.query(PlayerStat.season)
            .distinct()
            .order_by(PlayerStat.season.desc())
            .all()
        )

    def get_seasons(self):

        seasons = (
            self.db.query(PlayerStat.season)
            .distinct()
            .order_by(PlayerStat.season.desc())
            .all()
        )

        return [season[0] for season in seasons]