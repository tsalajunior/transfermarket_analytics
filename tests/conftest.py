from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


from datetime import date
from types import SimpleNamespace
from app.repositories.player_repository import PlayerRepository
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def repo():
    return PlayerRepository(None)


@pytest.fixture
def player():

    return SimpleNamespace(

        id=1,
        name="Kylian Mbappé",
        birth_date=date(1998, 12, 20),
        nationality="France",
        position="Centre-Forward",
        market_value_eur=180000000,

        club=SimpleNamespace(
            id=10,
            name="Real Madrid"
        )

    )


@pytest.fixture
def stats():

    return SimpleNamespace(

        season="25/26",
        competition="LaLiga",

        goals=35,
        assists=8,
        appearances=42,
        minutes_played=3300,

        goals_per_90=0.95,
        assists_per_90=0.22,
        goal_contribution_per_90=1.17

    )



@pytest.fixture
def client():
    return TestClient(app)