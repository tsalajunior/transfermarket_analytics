from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.repositories.league_repository import LeagueRepository

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
def get_seasons(
    db: Session = Depends(get_db)
):

    repository = LeagueRepository(db)

    return repository.get_seasons()