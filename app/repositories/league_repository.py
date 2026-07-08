from os import name

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.utils.date_utils import calculate_age
from app.models.club import Club    
from app.models.league import League
from app.models.player import Player
from app.models.stat import PlayerStat
from app.utils.date_utils import calculate_age
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
    
    
    def get_league_dashboard(
        self,
        league_id: int,
        season: str = "25/26"
    ):

        clubs = (
            self.db.query(Club)
            .filter(Club.league_id == league_id)
            .all()
        )

        club_ids = [club.id for club in clubs]

        total_market_value = (
            self.db.query(
                func.sum(Player.market_value_eur)
            )
            .filter(Player.club_id.in_(club_ids))
            .scalar()
            or 0
        )

        players = (
            self.db.query(Player)
            .filter(
                Player.club_id.in_(club_ids)
            )
            .all()
        )

        ages = []

        for player in players:

            age = calculate_age(player.birth_date)

            if age is not None:
                ages.append(age)

        average_age = (
            round(sum(ages) / len(ages), 2)
            if ages
            else 0
        )

        total_goals = (
            self.db.query(
                func.sum(PlayerStat.goals)
            )
            .join(Player)
            .filter(
                Player.club_id.in_(club_ids),
                PlayerStat.season == season
            )
            .scalar()
            or 0
        )

        total_assists = (
            self.db.query(
                func.sum(PlayerStat.assists)
            )
            .join(Player)
            .filter(
                Player.club_id.in_(club_ids),
                PlayerStat.season == season
            )
            .scalar()
            or 0
        )

        players_count = (
            self.db.query(Player)
            .filter(Player.club_id.in_(club_ids))
            .count()
        )

        return {

            "league": clubs[0].league.name if clubs else "",

            "country": clubs[0].league.country if clubs else "",

            "clubs": len(clubs),

            "players": players_count,

            "total_market_value": total_market_value,

            "average_age": round(float(average_age), 2),

            "goals": total_goals,

            "assists": total_assists

        }

    def get_club_market_values(
        self,
        league_id: int
    ):

        results = (

            self.db.query(

                Club.name,

                func.sum(Player.market_value_eur).label(
                    "market_value"
                )

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .filter(
                Club.league_id == league_id
            )

            .group_by(
                Club.id,
                Club.name
            )

            .order_by(
                func.sum(Player.market_value_eur).desc()
            )

            .all()

        )
        #
        print("=" * 50)
        print("Market values query:", results)
        print("=" * 50)

        return [

            {

                "club": row.name,

                "market_value": float(
                    row.market_value or 0
                )

            }

            for row in results

        ]
    
    def get_average_age_by_club(
        self,
        league_id: int
    ):

        clubs = (

            self.db.query(Club)

            .filter(
                Club.league_id == league_id
            )

            .all()

        )

        results = []

        for club in clubs:

            ages = [

                calculate_age(player.birth_date)

                for player in club.players

                if player.birth_date

            ]

            average_age = (

                round(sum(ages) / len(ages), 2)

                if ages

                else 0

            )

            results.append(

                {

                    "club": club.name,

                    "average_age": average_age

                }

            )

        return sorted(

            results,

            key=lambda x: x["average_age"]

        )
    
    def get_top_scorers(
        self,
        league_id: int,
        season: str,
        limit: int = 10
    ):

        results = (

            self.db.query(

                Player.name.label("player"),
                Club.name.label("club"),
                PlayerStat.goals

            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .join(
                Club,
                Player.club_id == Club.id
            )

            .filter(

                Club.league_id == league_id,

                PlayerStat.season == season

            )

            .order_by(
                PlayerStat.goals.desc()
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "player": row.player,
                "club": row.club,
                "goals": row.goals

            }

            for row in results

        ]
    
    def get_top_assists(
        self,
        league_id: int,
        season: str,
        limit: int = 10
    ):

        results = (

            self.db.query(

                Player.name.label("player"),
                Club.name.label("club"),
                PlayerStat.assists

            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .join(
                Club,
                Player.club_id == Club.id
            )

            .filter(

                Club.league_id == league_id,

                PlayerStat.season == season

            )

            .order_by(
                PlayerStat.assists.desc()
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "player": row.player,
                "club": row.club,
                "assists": row.assists

            }

            for row in results

        ]

    def get_most_offensive_clubs(
        self,
        league_id: int,
        season: str
    ):

        results = (

            self.db.query(

                Club.name.label("club"),

                func.sum(PlayerStat.goals).label("goals")

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(

                Club.league_id == league_id,

                PlayerStat.season == season

            )

            .group_by(
                Club.id,
                Club.name
            )

            .order_by(
                func.sum(PlayerStat.goals).desc()
            )

            .all()

        )

        return [

            {

                "club": row.club,
                "goals": int(row.goals or 0)

            }

            for row in results

        ]
    
    def get_most_creative_clubs(
        self,
        league_id: int,
        season: str
    ):

        results = (

            self.db.query(

                Club.name.label("club"),

                func.sum(PlayerStat.assists).label("assists")

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(

                Club.league_id == league_id,

                PlayerStat.season == season

            )

            .group_by(
                Club.id,
                Club.name
            )

            .order_by(
                func.sum(PlayerStat.assists).desc()
            )

            .all()

        )

        return [

            {

                "club": row.club,

                "assists": int(row.assists or 0)

            }

            for row in results

        ]
    
    def get_attack_scatter(
        self,
        league_id: int,
        season: str
    ):

        results = (

            self.db.query(

                Club.name.label("club"),

                func.sum(PlayerStat.goals).label("goals"),

                func.sum(PlayerStat.assists).label("assists")

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(

                Club.league_id == league_id,

                PlayerStat.season == season

            )

            .group_by(
                Club.id,
                Club.name
            )

            .all()

        )

        return [

            {

                "club": row.club,

                "goals": int(row.goals or 0),

                "assists": int(row.assists or 0)

            }

            for row in results

        ]