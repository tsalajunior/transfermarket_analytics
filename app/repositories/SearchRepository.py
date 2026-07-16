from sqlalchemy.orm import Session

from app.models.player import Player
from app.models.club import Club
from app.models.league import League


class SearchRepository:

    def __init__(self, db: Session):
        self.db = db

    def search_players(
        self,
        query: str,
        limit: int = 10
    ):

        players = (

            self.db.query(Player)

            .filter(
                Player.name.ilike(f"%{query}%")
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "type": "player",

                "id": player.id,

                "name": player.name,

                "club": player.club.name if player.club else None

            }

            for player in players

        ]

    def search_clubs(
        self,
        query: str,
        limit: int = 10
    ):

        clubs = (

            self.db.query(Club)

            .filter(
                Club.name.ilike(f"%{query}%")
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "type": "club",

                "id": club.id,

                "name": club.name

            }

            for club in clubs

        ]

    def search_leagues(
        self,
        query: str,
        limit: int = 10
    ):

        leagues = (

            self.db.query(League)

            .filter(
                League.name.ilike(f"%{query}%")
            )

            .limit(limit)

            .all()

        )

        return [

            {

                "type": "league",

                "id": league.id,

                "name": league.name

            }

            for league in leagues

        ]

    def global_search(
        self,
        query: str
    ):

        return {

            "players": self.search_players(query),

            "clubs": self.search_clubs(query),

            "leagues": self.search_leagues(query)

        }