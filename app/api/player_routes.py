from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.repositories.player_repository import PlayerRepository
from app.schemas.player import (
    TopScorerResponse,
    PlayerDetailsResponse,
    ComparisonResponse,
    PlayerListResponse
)

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get(
    "/top-scorers",
    response_model=list[TopScorerResponse]
)
def get_top_scorers(
    season: str = "25/26",
    limit: int = 20,
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    return repository.get_top_scorers(
        season=season,
        limit=limit
    )

@router.get("/top-goals-per-90")
def get_top_goals_per_90(
    season: str = "25/26",
    limit: int = 20,
    min_minutes: int = 500,
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    return repository.get_top_goals_per_90(
        season=season,
        limit=limit,
        min_minutes=min_minutes
    )


@router.get("/top-contributors-per-90")
def get_top_contributors_per_90(
    season: str = "25/26",
    limit: int = 20,
    min_minutes: int = 500,
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    return repository.get_top_contributors_per_90(
        season=season,
        limit=limit,
        min_minutes=min_minutes
    )

@router.get("/top-assists")
def get_top_assists(
    season: str = "25/26",
    limit: int = 20,
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    return repository.get_top_assists(
        season=season,
        limit=limit
    )

@router.get("/")
def get_players(
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    return repository.get_all_players()
    

@router.get("/search")
def search_players(
    q: str,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    repository = PlayerRepository(db)

    return repository.search_players(
        query=q,
        limit=limit
    )

@router.get("/club/{club_id}")
def get_club_players(
    club_id: int,
    db: Session = Depends(get_db)
):
    repository = PlayerRepository(db)

    return repository.get_players_by_club(
        club_id
    )


@router.get(
    "/compare",
    response_model=ComparisonResponse
)
def compare_players(
    player1: int,
    player2: int,
    season: str = "25/26",
    db: Session = Depends(get_db)
):

    repository = PlayerRepository(db)

    comparison = repository.compare_players(
        player1,
        player2,
        season
    )

    if comparison is None:
        raise HTTPException(
            status_code=404,
            detail="One or both players not found"
        )

    return comparison



@router.get(
    "/{player_id}",
    response_model=PlayerDetailsResponse
)
def get_player(
    player_id: int,
    season: str = "25/26",
    db: Session = Depends(get_db)
):
    repository = PlayerRepository(db)

    player = repository.get_player_details(
        player_id,
        season
    )

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    return player


@router.get("/most-valuable")
def get_most_valuable_players(

    limit: int = 20,

    db: Session = Depends(get_db)

):

    repository = PlayerRepository(db)

    return repository.get_most_valuable_players(
        limit
    )