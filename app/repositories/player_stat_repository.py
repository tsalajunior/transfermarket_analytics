from sqlalchemy.orm import Session

from app.models.stat import PlayerStat


class PlayerStatRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_if_not_exists(
        self,
        player_id: int,
        season: str,
        competition: str,
        appearances: int = 0,
        goals: int = 0,
        assists: int = 0,
        minutes_played: int = 0,
        yellow_cards: int = 0,
        red_cards: int = 0,
        club_id: int = None
    ):

        stat = (
            self.db.query(PlayerStat)
            .filter(
                PlayerStat.player_id == player_id,
                PlayerStat.season == season,
                PlayerStat.competition == competition
            )
            .first()
        )

        if stat:
            return stat

        stat = PlayerStat(
            player_id=player_id,
            club_id=club_id,
            season=season,
            competition=competition,
            appearances=appearances,
            goals=goals,
            assists=assists,
            minutes_played=minutes_played,
            yellow_cards=yellow_cards,
            red_cards=red_cards
        )

        self.db.add(stat)
        self.db.commit()
        self.db.refresh(stat)

        return stat