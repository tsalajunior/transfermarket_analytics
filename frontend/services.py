import requests

from config import API_URL


def get_clubs():
    try:
        response = requests.get(
            f"{API_URL}/clubs",
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        return []


def get_club(
    club_id,
    season
):

    response = requests.get(
        f"{API_URL}/clubs/{club_id}",
        params={
            "season": season
        }
    )

    return response.json()


def get_seasons():

    response = requests.get(
        f"{API_URL}/leagues/seasons"
    )

    return response.json()


def get_players_by_club(
    club_id,
    season
):
    response = requests.get(
        f"{API_URL}/clubs/{club_id}/players",
        params={"season": season}
    )

    return response.json()


def search_players(query: str):

    response = requests.get(
        f"{API_URL}/players/search",
        params={"q": query}
    )

    if response.status_code == 200:
        return response.json()

    return []

def get_players():

    response = requests.get(
        f"{API_URL}/players"
    )

    if response.status_code == 200:
        return response.json()

    return []

def get_player(
    player_id: int,
    season: str
):

    response = requests.get(
        f"{API_URL}/players/{player_id}",
        params={
            "season": season
        }
    )

    if response.status_code == 200:
        return response.json()

    return None


