from pydantic import BaseModel


class PlayerStatResponse(BaseModel):

    player_name: str

    appearances: int
    goals: int
    assists: int

    minutes_played: int

    goals_per_90: float | None = None
    assists_per_90: float | None = None
    goal_contributions_per_90: float | None = None

    class Config:
        from_attributes = True