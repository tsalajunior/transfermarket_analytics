from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.repositories.league_repository import LeagueRepository
from app.utils.constants import *
router = APIRouter(
    prefix="/leagues",
    tags=["Leagues"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/seasons")
def get_seasons(db: Session = Depends(get_db)):
    repository = LeagueRepository(db)
    return repository.get_seasons()


# -------- ROUTES SPECIFIQUES D'ABORD --------

@router.get("/{league_id}/market-values")
def get_market_values(
    league_id: int,
    db: Session = Depends(get_db)
):
    repository = LeagueRepository(db)
    return repository.get_club_market_values(league_id)


# -------- ROUTE GENERIQUE ENSUITE --------

@router.get("/{league_id}")
def get_league_dashboard(
    league_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)
):
    repository = LeagueRepository(db)
    return repository.get_league_dashboard(
        league_id,
        season
    )

@router.get("/{league_id}/average-age")
def get_average_age(
    league_id: int,
    db: Session = Depends(get_db)
):

    repository = LeagueRepository(db)

    return repository.get_average_age_by_club(
        league_id
    )

@router.get("/{league_id}/top-scorers")
def get_top_scorers(

    league_id: int,
    season: str = DEFAULT_SEASON,
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)

):

    repository = LeagueRepository(db)

    return repository.get_top_scorers(
        league_id,
        season,
        limit
    )

@router.get("/{league_id}/top-assists")
def get_top_assists(

    league_id: int,
    season: str = DEFAULT_SEASON,
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db)

):

    repository = LeagueRepository(db)

    return repository.get_top_assists(
        league_id,
        season,
        limit
    )


@router.get("/{league_id}/most-offensive")
def get_most_offensive_clubs(

    league_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)

):

    repository = LeagueRepository(db)

    return repository.get_most_offensive_clubs(
        league_id,
        season
    )

@router.get("/{league_id}/most-creative")
def get_most_creative(

    league_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)

):

    repository = LeagueRepository(db)

    return repository.get_most_creative_clubs(
        league_id,
        season
    )

@router.get("/{league_id}/attack-scatter")
def attack_scatter(

    league_id: int,
    season: str = DEFAULT_SEASON,
    db: Session = Depends(get_db)

):

    repository = LeagueRepository(db)

    return repository.get_attack_scatter(
        league_id,
        season
    )