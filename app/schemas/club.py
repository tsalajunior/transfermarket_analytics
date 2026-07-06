from pydantic import BaseModel
from typing import Optional


class ClubTopScorerResponse(BaseModel):
    name: str
    goals: int

    class Config:
        from_attributes = True


class ClubTopAssistResponse(BaseModel):
    name: str
    assists: int

    class Config:
        from_attributes = True


class ClubDetailsResponse(BaseModel):

    id: int
    name: str
    country: Optional[str]
    league: Optional[str]

    players_count: int

    top_scorer: Optional[ClubTopScorerResponse]
    top_assist: Optional[ClubTopAssistResponse]

    total_market_value: float
    average_market_value: float
    average_age: float
    total_goals: int
    total_assists: int

    class Config:
        from_attributes = True


class ClubMarketValueResponse(BaseModel):
    club: str
    market_value: float

class ClubGoalsResponse(BaseModel):
    club: str
    goals: int

class ClubAssistsResponse(BaseModel):
    club: str
    assists: int

class ClubAverageMarketValueResponse(BaseModel):
    club: str
    average_market_value: float

class ClubAverageAgeResponse(BaseModel):
    club: str
    average_age: float

class ClubListResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True