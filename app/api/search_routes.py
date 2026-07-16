from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.repositories.SearchRepository import SearchRepository


router = APIRouter(

    prefix="/search",

    tags=["Search"]

)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get("/")
def global_search(

    q: str,

    db: Session = Depends(get_db)

):

    repository = SearchRepository(db)

    return repository.global_search(q)