from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.core.database import SessionLocal
from app.repositories.DashboardRepository import DashboardRepository

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/summary")
def get_dashboard_summary(
    db: Session = Depends(get_db)
):

    repository = DashboardRepository(db)

    return repository.get_dashboard_summary()

@router.get("/market-value-by-club")
def get_market_value_by_club(

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_market_value_by_club()

@router.get("/position-distribution")
def get_position_distribution(

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_position_distribution()


@router.get("/average-age-by-club")
def get_average_age_by_club(

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_average_age_by_club()


@router.get("/top-nationalities")
def get_top_nationalities(

    limit: int = 10,

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_top_nationalities(limit)


@router.get("/average-market-value-position")
def get_average_market_value_position(

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_average_market_value_by_position()


@router.get("/top-scoring-clubs")
def get_top_scoring_clubs(

    limit: int = 10,

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_top_scoring_clubs(limit)

@router.get("/top-assist-clubs")
def get_dashboard_top_assist_clubs(

    limit: int = 10,

    db: Session = Depends(get_db)

):

    repository = DashboardRepository(db)

    return repository.get_dashboard_top_assist_clubs(limit)



