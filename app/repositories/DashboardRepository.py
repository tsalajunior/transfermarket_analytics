from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.club import Club
from app.models.player import Player
from app.models.stat import PlayerStat
from app.utils.date_utils import calculate_age


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_summary(self):

        total_clubs = (
            self.db.query(Club)
            .count()
        )

        total_players = (
            self.db.query(Player)
            .count()
        )

        total_goals = (
            self.db.query(
                func.sum(PlayerStat.goals)
            )
            .scalar() or 0
        )

        total_assists = (
            self.db.query(
                func.sum(PlayerStat.assists)
            )
            .scalar() or 0
        )

        players = (
            self.db.query(Player.birth_date)
            .all()
        )

        ages = [
            calculate_age(player.birth_date)
            for player in players
            if player.birth_date
        ]

        average_age = (
            sum(ages) / len(ages)
            if ages
            else 0
        )

        average_market_value = (
            self.db.query(
                func.avg(Player.market_value_eur)
            )
            .scalar()
        )

        total_market_value = (
            self.db.query(
                func.sum(Player.market_value_eur)
            )
            .scalar()
        )

        return {

            "clubs": total_clubs,

            "players": total_players,

            "goals": int(total_goals),

            "assists": int(total_assists),

            "average_age": round(float(average_age or 0), 1),

            "average_market_value": float(
                average_market_value or 0
            ),

            "total_market_value": float(
                total_market_value or 0
            )

        }

    def get_market_value_by_club(self):

        results = (

            self.db.query(

                Club.name,

                func.sum(Player.market_value_eur).label("market_value")

            )

            .join(
                Player,
                Club.id == Player.club_id
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

        return [

            {

                "club": row.name,

                "market_value": float(row.market_value or 0)

            }

            for row in results

        ]
    
    def get_position_distribution(self):

        results = (

            self.db.query(

                Player.position,

                func.count(Player.id).label("count")

            )

            .group_by(Player.position)

            .order_by(func.count(Player.id).desc())

            .all()

        )

        return [

            {

                "position": row.position,

                "count": row.count

            }

            for row in results

        ]

    def get_average_age_by_club(self):

        players = (

            self.db.query(

                Club.name,

                Player.birth_date

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .filter(
                Player.birth_date.isnot(None)
            )

            .all()

        )

        clubs = {}

        for club_name, birth_date in players:

            age = calculate_age(birth_date)

            if age is None:
                continue

            clubs.setdefault(club_name, []).append(age)

        result = []

        for club, ages in clubs.items():

            result.append(

                {

                    "club": club,

                    "average_age": round(sum(ages) / len(ages), 1)

                }

            )

        return sorted(

            result,

            key=lambda x: x["average_age"],

            reverse=True

        )
    
    def get_top_nationalities(
        self,
        limit: int = 10
    ):

        results = (

            self.db.query(

                Player.nationality,

                func.count(Player.id).label("players")

            )

            .filter(
                Player.nationality.isnot(None)
            )

            .group_by(
                Player.nationality
            )

            .order_by(
                func.count(Player.id).desc()
            )

            .limit(limit)

            .all()

        )

        return [

            {
                "nationality": nationality,
                "players": players
            }

            for nationality, players in results

        ]

    def get_average_market_value_by_position(self):

        results = (

            self.db.query(

                Player.position,

                func.avg(
                    Player.market_value_eur
                ).label("average_value")

            )

            .filter(
                Player.market_value_eur.isnot(None)
            )

            .group_by(
                Player.position
            )

            .order_by(
                func.avg(
                    Player.market_value_eur
                ).desc()
            )

            .all()

        )

        return [

            {

                "position": position,

                "average_value": float(value)

            }

            for position, value in results

        ]

    def get_top_scoring_clubs(
        self,
        limit: int = 10
    ):

        results = (

            self.db.query(

                Club.name,

                func.sum(
                    PlayerStat.goals
                ).label("goals")

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .group_by(
                Club.name
            )

            .order_by(
                func.sum(
                    PlayerStat.goals
                ).desc()
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "club": club,

                "goals": int(goals or 0)

            }

            for club, goals in results

        ]

    def get_dashboard_top_assist_clubs(
        self,
        limit: int = 10
    ):

        results = (

            self.db.query(

                Club.name,

                func.sum(
                    PlayerStat.assists
                ).label("assists")

            )

            .join(
                Player,
                Club.id == Player.club_id
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .group_by(
                Club.name
            )

            .order_by(
                func.sum(
                    PlayerStat.assists
                ).desc()
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "club": club,

                "assists": int(assists or 0)

            }

            for club, assists in results

        ]

