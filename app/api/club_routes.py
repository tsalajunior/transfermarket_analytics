from fastapi import APIRouter, Depends, HTTPException
from app.schemas.club import (
    ClubDetailsResponse,
    ClubMarketValueResponse,
    ClubGoalsResponse,
    ClubAssistsResponse,
    ClubAverageMarketValueResponse,
    ClubAverageAgeResponse,
    ClubListResponse,
)
from app.schemas.player import ClubPlayerResponse
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from app.repositories.club_repository import ClubRepository
from app.utils.constants import *


router = APIRouter(
    prefix="/clubs",
    tags=["Clubs"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get(
    "",
    response_model=list[ClubListResponse]
)
def get_all_clubs(
    db: Session = Depends(get_db)
):
    repository = ClubRepository(db)

    return repository.get_all_clubs()


@router.get(
    "/{club_id}/players",
    response_model=list[ClubPlayerResponse]
)
def get_players_by_club(
    club_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_players_by_club(
        club_id,
        season
    )

@router.get(
    "/market-value",
    response_model=list[ClubMarketValueResponse]
)
def get_clubs_market_value(
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_clubs_market_value(
        limit=limit
    )

@router.get(
    "/top-attacks",
    response_model=list[ClubGoalsResponse]
)
def get_top_attacks(
    season: str = DEFAULT_SEASON,
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_top_attacks(
        season=season,
        limit=limit
    )


@router.get(
    "/top-assists",
    response_model=list[ClubAssistsResponse]
)
def get_top_assists(
    season: str = DEFAULT_SEASON,
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_top_assists(
        season=season,
        limit=limit
    )


@router.get(
    "/average-market-value",
    response_model=list[ClubAverageMarketValueResponse]
)
def get_average_market_value(
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_average_market_value(
        limit=limit
    )


@router.get(
    "/average-age",
    response_model=list[ClubAverageAgeResponse]
)
def get_average_age(
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    return repository.get_average_age(
        limit=limit
    )

@router.get(
    "/{club_id}",
    response_model=ClubDetailsResponse
)
def get_club(
    club_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)
):

    repository = ClubRepository(db)

    club = repository.get_club_details(
        club_id=club_id,
        season=season
    )

    if club is None:
        raise HTTPException(
            status_code=404,
            detail="Club not found"
        )

    return club