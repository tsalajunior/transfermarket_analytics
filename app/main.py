from fastapi import FastAPI

from app.api.player_routes import router as player_router
from app.api.club_routes import router as club_router
from app.api import league_routes
from app.api.dashboard_routes import router as dashboard_router
from app.api.search_routes import router as search_router


app = FastAPI(
    title="Transfermarkt Analytics API"
)

app.include_router(player_router)
app.include_router(club_router)
app.include_router(league_routes.router)
app.include_router(dashboard_router)
app.include_router(search_router)