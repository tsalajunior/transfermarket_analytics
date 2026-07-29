from fastapi import status

from app.repositories.league_repository import LeagueRepository


def test_get_seasons(client, mocker):

    expected = [
        "25/26",
        "24/25",
        "23/24"
    ]

    mocker.patch.object(
        LeagueRepository,
        "get_seasons",
        return_value=expected
    )

    response = client.get("/leagues/seasons")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_league_dashboard(client, mocker):

    expected = {

        "league": "LaLiga",
        "country": "Spain",

        "clubs": 20,
        "players": 520,

        "total_market_value": 5230000000.0,

        "average_age": 26.4,

        "goals": 931,
        "assists": 642

    }

    mocker.patch.object(
        LeagueRepository,
        "get_league_dashboard",
        return_value=expected
    )

    response = client.get("/leagues/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_league_dashboard_not_found(client, mocker):

    mocker.patch.object(
        LeagueRepository,
        "get_league_dashboard",
        return_value=None
    )

    response = client.get("/leagues/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "League not found"


def test_get_market_values(client, mocker):

    expected = [

        {

            "club": "Real Madrid",

            "market_value": 1320000000.0

        }

    ]

    mocker.patch.object(
        LeagueRepository,
        "get_club_market_values",
        return_value=expected
    )

    response = client.get("/leagues/1/market-values")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_average_age(client, mocker):

    expected = [

        {

            "club": "Real Madrid",

            "average_age": 26.8

        }

    ]

    mocker.patch.object(
        LeagueRepository,
        "get_average_age_by_club",
        return_value=expected
    )

    response = client.get("/leagues/1/average-age")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_top_scorers(client, mocker):

    expected = [

        {

            "player": "Kylian Mbappé",

            "club": "Real Madrid",

            "goals": 35

        }

    ]

    mocker.patch.object(
        LeagueRepository,
        "get_top_scorers",
        return_value=expected
    )

    response = client.get("/leagues/1/top-scorers")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_top_assists(client, mocker):

    expected = [

        {

            "player": "Lamine Yamal",

            "club": "FC Barcelona",

            "assists": 16

        }

    ]

    mocker.patch.object(
        LeagueRepository,
        "get_top_assists",
        return_value=expected
    )

    response = client.get("/leagues/1/top-assists")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected