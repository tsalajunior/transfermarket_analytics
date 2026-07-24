from sqlalchemy.orm import Session
from app.utils.date_utils import calculate_age
from app.models.player import Player
from app.models.stat import PlayerStat


class PlayerRepository:

    def __init__(self, db: Session):
        self.db = db

    """
        Builders
    """
    def _build_player_list(self, player: Player):
        return {
            "id": player.id,
            "name": player.name,
            "club": player.club.name if player.club else None,
        }

    def _build_comparison_player(
        self,
        player: Player,
        stats: PlayerStat | None
    ):
        return {
            "id": player.id,
            "name": player.name,
            "age": calculate_age(player.birth_date),
            "nationality": player.nationality,
            "position": player.position,
            "club": player.club.name if player.club else None,
            "market_value_eur": (
                float(player.market_value_eur)
                if player.market_value_eur
                else None
            ),

            "goals": stats.goals if stats else 0,
            "assists": stats.assists if stats else 0,
            "appearances": stats.appearances if stats else 0,
            "minutes_played": stats.minutes_played if stats else 0,

            "goals_per_90": stats.goals_per_90 if stats else 0,
            "assists_per_90": stats.assists_per_90 if stats else 0,
            "goal_contribution_per_90": (
                stats.goal_contribution_per_90 if stats else 0
            ),
        }

    def _build_player_summary(
        self,
        player: Player,
        stats: PlayerStat
    ):
        return {
            "id": player.id,
            "player": player.name,

            "age": calculate_age(player.birth_date),
            "nationality": player.nationality,
            "club": player.club.name if player.club else None,
            "position": player.position,

            "market_value": (
                float(player.market_value_eur)
                if player.market_value_eur
                else None
            ),

            "goals": stats.goals,
            "assists": stats.assists,
            "appearances": stats.appearances,
            "minutes_played": stats.minutes_played,

            "goals_per_90": stats.goals_per_90,
            "assists_per_90": stats.assists_per_90,
            "goal_contribution_per_90": stats.goal_contribution_per_90,
        }

    def _get_player_with_stats(
        self,
        player_id: int,
        season: str = "25/26"
    ):

        return (
            self.db.query(
                Player,
                PlayerStat
            )
            .outerjoin(
                PlayerStat,
                (
                    (Player.id == PlayerStat.player_id)
                    &
                    (PlayerStat.season == season)
                )
            )
            .filter(
                Player.id == player_id
            )
            .first()
        )
    
    def get_by_tm_id(self, tm_id: str):
        return (
            self.db.query(Player)
            .filter(Player.tm_id == tm_id)
            .first()
        )

    def create_if_not_exists(
        self,
        tm_id: str,
        name: str,
        nationality: str = None,
        position: str = None,
        market_value_eur: float = None,
        url: str = None,
        club_id: int = None
    ):

        player = self.get_by_tm_id(tm_id)

        if player:

            if player.url is None:
                player.url = url

            return player

        # player = Player(
        #     tm_id=tm_id,
        #     name=name,
        #     nationality=nationality,
        #     position=position,
        #     market_value_eur=market_value_eur,
        #     url=url,
        #     club_id=club_id
        # )

        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)

        return player
    
    def get_top_scorers(
        self,
        season: str = "25/26",
        limit: int = 20
    ):

        results = (
            self.db.query(
                Player.name,
                PlayerStat.goals
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                PlayerStat.season == season
            )
            .order_by(
                PlayerStat.goals.desc()
            )
            .limit(limit)
            .all()
        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]
            
    def get_top_assists(
        self,
        season: str = "25/26",
        limit: int = 20
    ):
        results = (
            self.db.query(
                Player.name,
                PlayerStat.assists
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                PlayerStat.season == season
            )
            .order_by(
                PlayerStat.assists.desc()
            )
            .limit(limit)
            .all()
        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]
    
    def get_top_goals_per_90(
        self,
        season: str = "25/26",
        limit: int = 20,
        min_minutes: int = 500
    ):

        results = (
            self.db.query(
                Player.name,
                PlayerStat.goals_per_90
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                PlayerStat.season == season
            )
            .filter(
                PlayerStat.minutes_played >= min_minutes
            )
            .order_by(
                PlayerStat.goals_per_90.desc()
            )
            .limit(limit)
            .all()
        )

        return [
            {
                "name": row.name,
                "goals_per_90": row.goals_per_90
            }
            for row in results
        ]        

    def get_top_contributors_per_90(
        self,
        season: str = "25/26",
        limit: int = 20,
        min_minutes: int = 500
    ):

        results = (
            self.db.query(
                Player.name,
                PlayerStat.goal_contribution_per_90
            )
            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )
            .filter(
                PlayerStat.season == season
            )
            .filter(
                PlayerStat.minutes_played >= min_minutes
            )
            .order_by(
                PlayerStat.goal_contribution_per_90.desc()
            )
            .limit(limit)
            .all()
        )

        return [
            {
                "name": row.name,
                "goal_contribution_per_90": row.goal_contribution_per_90
            }
            for row in results
        ]
    
    def search_players(
        self,
        query: str,
        limit: int = 20
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
                "id": player.id,
                "name": player.name,
                "nationality": player.nationality,
                "position": player.position
            }
            for player in players
        ]

    def get_player_details(
        self,
        player_id: int,
        season: str = "25/26"
    ):

        player = (
            self.db.query(Player)
            .filter(Player.id == player_id)
            .first()
        )

        if not player:
            return None

        stats = (
            self.db.query(PlayerStat)
            .filter(
                PlayerStat.player_id == player_id,
                PlayerStat.season == season
            )
            .first()
        )

        return {
            "id": player.id,
            "name": player.name,
            "birth_date": player.birth_date,
            "nationality": player.nationality,
            "position": player.position,
            "market_value_eur": float(player.market_value_eur)
            if player.market_value_eur is not None
            else None,

            "club": {
                "id": player.club.id,
                "name": player.club.name
            } if player.club else None,

            "stats": {
                "season": stats.season,
                "competition": stats.competition,
                "appearances": stats.appearances,
                "goals": stats.goals,
                "assists": stats.assists,
                "minutes_played": stats.minutes_played,
                "goals_per_90": stats.goals_per_90,
                "assists_per_90": stats.assists_per_90,
                "goal_contribution_per_90": stats.goal_contribution_per_90
            } if stats else None
        }

    def get_players_by_club(
        self,
        club_id: int
    ):
        players = (
            self.db.query(Player)
            .filter(
                Player.club_id == club_id
            )
            .all()
        )

        return [
            {
                "id": player.id,
                "name": player.name,
                "position": player.position,
                "market_value_eur": player.market_value_eur,
                "age": calculate_age(player.birth_date),
            }
            for player in players
        ]
    
    def compare_players(
        self,
        player1_id: int,
        player2_id: int,
        season: str = "25/26"
    ):

        result1 = self._get_player_with_stats(player1_id, season)
        result2 = self._get_player_with_stats(player2_id, season)

        if result1 is None or result2 is None:
            return None

        player1, stats1 = result1
        player2, stats2 = result2

        return {
            "player1": self._build_comparison_player(player1, stats1),
            "player2": self._build_comparison_player(player2, stats2),
        }

    def get_all_players(self):

        players = (
            self.db.query(Player)
            .order_by(Player.name)
            .all()
        )

        return [
            self._build_player_list(player)
            for player in players
        ]
    
    def get_most_valuable_players(
        self,
        limit: int = 20,
        club: str | None = None 
    ):
        
        query = (
            self.db.query(Player)
            .filter(Player.market_value_eur.isnot(None))
        )

        if club and club != "All":
            query = query.filter(
                Player.club.has(name=club)
            )

        players = (
            query
            .order_by(Player.market_value_eur.desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "player": player.name,
                "age": calculate_age(player.birth_date),
                "nationality": player.nationality,
                "club": player.club.name if player.club else None,
                "position": player.position,
                "market_value": float(player.market_value_eur)
            }
            for player in players
        ]

    def get_player_ranking_scorers(
        self,
        season: str = "25/26",
        limit: int = 20,
        position: str | None = None,
        club=None,
        min_minutes: int = 0
    ):

        query = (

            self.db.query(
                Player,
                PlayerStat
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(
                PlayerStat.season == season,
                PlayerStat.minutes_played >= min_minutes
            )

        )
        if club and club != "All":

            query = query.filter(
                Player.club.has(name=club)
            )

        if position and position != "All":

            query = query.filter(
                Player.position == position
            )

        results = (

            query

            .order_by(
                PlayerStat.goals.desc()
            )

            .limit(limit)

            .all()

        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]
        
    def get_player_ranking_assists(
        self,
        season: str = "25/26",
        limit: int = 20,
        position: str | None = None,
        club=None,
        min_minutes: int = 0
    ):

        query = (

            self.db.query(
                Player,
                PlayerStat
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(
                PlayerStat.season == season,
                PlayerStat.minutes_played >= min_minutes
            )

        )

        if club and club != "All":

            query = query.filter(
                Player.club.has(name=club)
            )

        if position and position != "All":

            query = query.filter(
                Player.position == position
            )

        results = (

            query

            .order_by(
                PlayerStat.assists.desc()
            )

            .limit(limit)

            .all()

        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]
            
    def get_top_goals_per90(
        self,
        season: str = "25/26",
        limit: int = 20,
        position: str | None = None,
        club=None,
        min_minutes: int = 0
    ):

        query = (

            self.db.query(
                Player,
                PlayerStat
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(
                PlayerStat.season == season,
                PlayerStat.minutes_played >= min_minutes
            )

        )

        if club and club != "All":

            query = query.filter(
                Player.club.has(name=club)
            )

        if position and position != "All":

            query = query.filter(
                Player.position == position
            )

        results = (

            query

            .order_by(
                PlayerStat.goals_per_90.desc()
            )

            .limit(limit)

            .all()

        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]

    def get_top_contributions_per90(
        self,
        season: str = "25/26",
        limit: int = 20,
        position: str | None = None,
        club=None,
        min_minutes: int = 0
    ):

        query = (

            self.db.query(
                Player,
                PlayerStat
            )

            .join(
                PlayerStat,
                Player.id == PlayerStat.player_id
            )

            .filter(
                PlayerStat.season == season,
                PlayerStat.minutes_played >= min_minutes
            )

        )

        if club and club != "All":

            query = query.filter(
                Player.club.has(name=club)
            )

        if position and position != "All":

            query = query.filter(
                Player.position == position
            )

        results = (

            query

            .order_by(
                PlayerStat.goal_contribution_per_90.desc()
            )

            .limit(limit)

            .all()

        )

        return [
            self._build_player_summary(player, stats)
            for player, stats in results
        ]



