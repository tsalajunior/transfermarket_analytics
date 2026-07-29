from fastapi.testclient import TestClient

from app.main import app
from app.repositories.club_repository import ClubRepository


def test_get_all_clubs(client, mocker):

    fake_clubs = [
        {
            "id": 1,
            "name": "Real Madrid"
        },
        {
            "id": 2,
            "name": "FC Barcelona"
        }
    ]

    mocker.patch.object(
        ClubRepository,
        "get_all_clubs",
        return_value=fake_clubs
    )

    response = client.get("/clubs")

    assert response.status_code == 200
    assert response.json() == fake_clubs

def test_get_club(client, mocker):

    fake_club = {

        "id": 1,
        "name": "Real Madrid",
        "country": "Spain",
        "league": "LaLiga",

        "players_count": 25,

        "top_scorer": {
            "name": "Mbappé",
            "goals": 35
        },

        "top_assist": {
            "name": "Vinicius",
            "assists": 15
        },

        "total_market_value": 1250000000.0,
        "average_market_value": 50000000.0,
        "average_age": 26.4,
        "total_goals": 90,
        "total_assists": 63

    }

    mocker.patch.object(
        ClubRepository,
        "get_club_details",
        return_value=fake_club
    )

    response = client.get("/clubs/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Real Madrid"

def test_get_club_not_found(client, mocker):

    mocker.patch.object(
        ClubRepository,
        "get_club_details",
        return_value=None
    )

    response = client.get("/clubs/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Club not found"
    }

def test_get_players_by_club(client, mocker):

    fake_players = [

        {
            "id": 1,
            "name": "Mbappé",
            "position": "Centre-Forward",
            "market_value_eur": 180000000,

            "goals": 35,
            "assists": 8,
            "appearances": 42,
            "minutes_played": 3300,

            "goals_per_90": 0.95,
            "assists_per_90": 0.22,
            "goal_contribution_per_90": 1.17
        }

    ]

    mocker.patch.object(
        ClubRepository,
        "get_players_by_club",
        return_value=fake_players
    )

    response = client.get("/clubs/1/players")

    assert response.status_code == 200
    assert response.json() == fake_players

def test_get_top_attacks(client, mocker):

    fake_result = [

        {
            "club": "Real Madrid",
            "goals": 90
        }

    ]

    mocker.patch.object(
        ClubRepository,
        "get_top_attacks",
        return_value=fake_result
    )

    response = client.get("/clubs/top-attacks")

    assert response.status_code == 200
    assert response.json() == fake_result

def test_get_top_assists(client, mocker):

    fake_result = [

        {
            "club": "Real Madrid",
            "assists": 63
        }

    ]

    mocker.patch.object(
        ClubRepository,
        "get_top_assists",
        return_value=fake_result
    )

    response = client.get("/clubs/top-assists")

    assert response.status_code == 200
    assert response.json() == fake_result

def test_get_average_market_value(client, mocker):

    fake_result = [

        {
            "club": "Real Madrid",
            "average_market_value": 50000000.0
        }

    ]

    mocker.patch.object(
        ClubRepository,
        "get_average_market_value",
        return_value=fake_result
    )

    response = client.get("/clubs/average-market-value")

    assert response.status_code == 200
    assert response.json() == fake_result

def test_get_average_age(client, mocker):

    fake_result = [

        {
            "club": "Real Madrid",
            "average_age": 26.4
        }

    ]

    mocker.patch.object(
        ClubRepository,
        "get_average_age",
        return_value=fake_result
    )

    response = client.get("/clubs/average-age")

    assert response.status_code == 200
    assert response.json() == fake_result

