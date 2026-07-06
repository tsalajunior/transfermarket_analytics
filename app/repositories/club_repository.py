from sqlalchemy.orm import Session

from sqlalchemy import func
from app.models.club import Club
from app.models.player import Player
from app.models.stat import PlayerStat


class ClubRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_tm_id(self, tm_id: str):
        return (
            self.db.query(Club)
            .filter(Club.tm_id == tm_id)
            .first()
        )

    def create(self, club: Club):
        self.db.add(club)
        self.db.commit()
        self.db.refresh(club)
        return club

    def create_if_not_exists(
        self,
        tm_id: str,
        name: str,
        url: str = None,
        country: str = None,
        league_id: int = None
    ):

        club = self.get_by_tm_id(tm_id)

        if club:

            if club.league_id is None:
                club.league_id = league_id

            if club.country is None:
                club.country = country

            if club.url is None:
                club.url = url

            self.db.commit()
            self.db.refresh(club)

            return club

        club = Club(
            tm_id=tm_id,
            name=name,
            url=url,
            country=country,
            league_id=league_id
        )

        self.db.add(club)
        self.db.commit()
        self.db.refresh(club)

        return club
    
    def get_club_details(
        self,
        club_id: int,
        season: str = "25/26"
    ):

        club = (
            self.db.query(Club)
            .filter(Club.id == club_id)
            .first()
        )

        if not club:
            return None

        players_count = (
            self.db.query(Player)
            .filter(Player.club_id == club_id)
            .count()
        )

        team_stats = (
            self.db.query(
                func.sum(Player.market_value_eur).label("market_value"),
                func.avg(Player.market_value_eur).label("average_market_value"),
                func.avg(
                    func.extract(
                        "year",
                        func.age(Player.birth_date)
                    )
                ).label("average_age"),
                func.sum(PlayerStat.goals).label("goals"),
                func.sum(PlayerStat.assists).label("assists")
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                Player.club_id == club_id,
                PlayerStat.season == season
            )
            .first()
        )

        top_scorer = (
            self.db.query(
                Player.name,
                PlayerStat.goals
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                Player.club_id == club_id,
                PlayerStat.season == season
            )
            .order_by(
                PlayerStat.goals.desc()
            )
            .first()
        )

        top_assist = (
            self.db.query(
                Player.name,
                PlayerStat.assists
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                Player.club_id == club_id,
                PlayerStat.season == season
            )
            .order_by(
                PlayerStat.assists.desc()
            )
            .first()
        )

        return {
            "id": club.id,
            "name": club.name,
            "country": club.country,
            "league": club.league.name if club.league else None,
            "players_count": players_count,
            "top_scorer": (
                {
                    "name": top_scorer.name,
                    "goals": top_scorer.goals
                }
                if top_scorer else None
            ),
            "top_assist": (
                {
                    "name": top_assist.name,
                    "assists": top_assist.assists
                }
                if top_assist else None
            ),
            "total_market_value": float(
                team_stats.market_value or 0
            ),

            "average_market_value": float(
                team_stats.average_market_value or 0
            ),

            "average_age": round(
                float(team_stats.average_age or 0),
                1
            ),

            "total_goals": int(
                team_stats.goals or 0
            ),

            "total_assists": int(
                team_stats.assists or 0
            ),
        }
  
    def get_clubs_market_value(
        self,
        limit: int = 20
    ):

        return (
            self.db.query(
                Club.name.label("club"),
                func.sum(Player.market_value_eur).label("market_value")
            )
            .join(
                Player,
                Player.club_id == Club.id
            )
            .group_by(
                Club.id,
                Club.name
            )
            .order_by(
                func.sum(Player.market_value_eur).desc()
            )
            .limit(limit)
            .all()
        )
    
    def get_top_attacks(
        self,
        season: str = "25/26",
        limit: int = 20
    ):

        return (
            self.db.query(
                Club.name.label("club"),
                func.sum(PlayerStat.goals).label("goals")
            )
            .join(
                Player,
                Player.club_id == Club.id
            )
            .join(
                PlayerStat,
                PlayerStat.player_id == Player.id
            )
            .filter(
                PlayerStat.season == season
            )
            .group_by(
                Club.id,
                Club.name
            )
            .order_by(
                func.sum(PlayerStat.goals).desc()
            )
            .limit(limit)
            .all()
        )

    def get_top_assists(
    self,
    season: str = "25/26",
    limit: int = 20
):

        return (
            self.db.query(
                Club.name.label("club"),
                func.sum(PlayerStat.assists).label("assists")
            )
            .join(
                Player,
                Player.club_id == Club.id
            )
            .join(
                PlayerStat,
                PlayerStat.player_id == Player.id
            )
            .filter(
                PlayerStat.season == season
            )
            .group_by(
                Club.id,
                Club.name
            )
            .order_by(
                func.sum(PlayerStat.assists).desc()
            )
            .limit(limit)
            .all()
        )

    def get_average_market_value(
        self,
        limit: int = 20
    ):

        return (
            self.db.query(
                Club.name.label("club"),
                func.avg(Player.market_value_eur).label("average_market_value")
            )
            .join(
                Player,
                Player.club_id == Club.id
            )
            .filter(
                Player.market_value_eur.isnot(None)
            )
            .group_by(
                Club.id,
                Club.name
            )
            .order_by(
                func.avg(Player.market_value_eur).desc()
            )
            .limit(limit)
            .all()
        )

    def get_average_age(
        self,
        limit: int = 20
    ):

        return (
            self.db.query(
                Club.name.label("club"),
                func.round(
                    func.avg(
                        func.extract(
                            "year",
                            func.age(Player.birth_date)
                        )
                    ),
                    2
                ).label("average_age")
            )
            .join(
                Player,
                Player.club_id == Club.id
            )
            .filter(
                Player.birth_date.isnot(None)
            )
            .group_by(
                Club.id,
                Club.name
            )
            .order_by(
                func.avg(
                    func.extract(
                        "year",
                        func.age(Player.birth_date)
                    )
                )
            )
            .limit(limit)
            .all()
        )
    
    def get_all_clubs(self):
        return (
            self.db.query(Club)
            .order_by(Club.name)
            .all()
        )
    
    def get_players_by_club(
        self,
        club_id: int,
        season: str = "25/26"
    ):

        return (
            self.db.query(
                Player.id,
                Player.name,
                Player.position,
                Player.market_value_eur,

                PlayerStat.appearances,
                PlayerStat.goals,
                PlayerStat.assists,
                PlayerStat.minutes_played,
                PlayerStat.goals_per_90,
                PlayerStat.assists_per_90,
                PlayerStat.goal_contribution_per_90
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                Player.club_id == club_id,
                PlayerStat.season == season
            )
            .order_by(
                PlayerStat.goals.desc(),
                PlayerStat.assists.desc(),
                Player.name
            )
            .all()
        )