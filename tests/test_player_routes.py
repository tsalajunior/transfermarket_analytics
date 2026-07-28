from fastapi.testclient import TestClient

from app.main import app
from app.repositories.player_repository import PlayerRepository

client = TestClient(app)

def test_get_players(mocker):

    fake_players = [
        {
            "id": 1,
            "name": "Mbappé"
        },
        {
            "id": 2,
            "name": "Vinicius"
        }
    ]

    mocker.patch.object(
        PlayerRepository,
        "get_all_players",
        return_value=fake_players
    )

    response = client.get("/players")

    assert response.status_code == 200

    assert response.json() == fake_players

def test_search_players(mocker):

    fake_result = [
        {
            "id": 1,
            "name": "Mbappé"
        }
    ]

    mock = mocker.patch.object(
        PlayerRepository,
        "search_players",
        return_value=fake_result
    )

    response = client.get(
        "/players/search?q=Mbappé&limit=5"
    )

    assert response.status_code == 200

    assert response.json() == fake_result

    mock.assert_called_once_with(
        query="Mbappé",
        limit=5
    )

def test_get_player(mocker):

    fake_player = {

        "id": 1,
        "name": "Mbappé",

        "birth_date": None,
        "nationality": "France",
        "position": "Centre-Forward",
        "market_value_eur": 180000000,

        "club": {
            "id": 10,
            "name": "Real Madrid"
        },

        "stats": {

            "season": "25/26",
            "competition": "LaLiga",

            "appearances": 42,
            "goals": 35,
            "assists": 8,
            "minutes_played": 3300,

            "goals_per_90": 0.95,
            "assists_per_90": 0.22,
            "goal_contribution_per_90": 1.17

        }

    }

    mocker.patch.object(
        PlayerRepository,
        "get_player_details",
        return_value=fake_player
    )

    response = client.get(
        "/players/1"
    )

    assert response.status_code == 200

    assert response.json()["name"] == "Mbappé"

def test_get_player_not_found(mocker):

    mocker.patch.object(
        PlayerRepository,
        "get_player_details",
        return_value=None
    )

    response = client.get(
        "/players/99999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Player not found"
    }

def test_compare_players(mocker):

    fake_comparison = {

        "player1": {

            "id": 1,
            "name": "Mbappé",
            "nationality": "France",
            "age": 27,
            "position": "Centre-Forward",
            "club": "Real Madrid",

            "goals": 35,
            "assists": 8,
            "appearances": 42,
            "minutes_played": 3300,

            "goals_per_90": 0.95,
            "assists_per_90": 0.22,
            "goal_contribution_per_90": 1.17,

            "market_value_eur": 180000000.0

        },

        "player2": {

            "id": 2,
            "name": "Vinicius",
            "nationality": "Brazil",
            "age": 26,
            "position": "Left Winger",
            "club": "Real Madrid",

            "goals": 22,
            "assists": 15,
            "appearances": 40,
            "minutes_played": 3200,

            "goals_per_90": 0.62,
            "assists_per_90": 0.42,
            "goal_contribution_per_90": 1.04,

            "market_value_eur": 170000000.0

        }

    }

    mock = mocker.patch.object(
        PlayerRepository,
        "compare_players",
        return_value=fake_comparison
    )

    response = client.get(
        "/players/compare?player1=1&player2=2"
    )

    assert response.status_code == 200

    assert response.json() == fake_comparison

    mock.assert_called_once_with(
        1,
        2,
        "25/26"
    )

def test_compare_players_not_found(mocker):

    mocker.patch.object(
        PlayerRepository,
        "compare_players",
        return_value=None
    )

    response = client.get(
        "/players/compare?player1=1&player2=999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "One or both players not found"
    }

