from pydantic import BaseModel
from typing import Optional
from datetime import date


class TopScorerResponse(
    BaseModel
):
    name: str
    goals: int

class ClubResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class PlayerStatsResponse(BaseModel):
    season: str
    competition: str

    appearances: int
    goals: int
    assists: int
    minutes_played: int

    goals_per_90: float | None
    assists_per_90: float | None
    goal_contribution_per_90: float | None

    class Config:
        from_attributes = True


class PlayerDetailsResponse(BaseModel):

    id: int

    name: str

    birth_date: Optional[date]

    nationality: Optional[str]

    position: Optional[str]

    market_value_eur: Optional[float]

    club: Optional[ClubResponse]

    stats: Optional[PlayerStatsResponse]

    class Config:
        from_attributes = True

class ComparisonPlayer(BaseModel):
    id: int
    name: str
    nationality: str | None
    position: str | None
    club: str | None

    goals: int
    assists: int
    appearances: int
    minutes_played: int

    goals_per_90: float | None
    assists_per_90: float | None
    goal_contribution_per_90: float | None

    market_value_eur: float | None


class ComparisonResponse(BaseModel):
    player1: ComparisonPlayer
    player2: ComparisonPlayer

class ClubPlayerResponse(BaseModel):

    id: int
    name: str
    position: str | None
    market_value_eur: float | None

    goals: int
    assists: int
    appearances: int
    minutes_played: int

    goals_per_90: float | None
    assists_per_90: float | None
    goal_contribution_per_90: float | None

    class Config:
        from_attributes = True

class PlayerListResponse(BaseModel):
    id: int
    name: str