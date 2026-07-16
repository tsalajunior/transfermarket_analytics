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

def compare_players(
    player1: int,
    player2: int,
    season: str
):

    response = requests.get(
        f"{API_URL}/players/compare",
        params={
            "player1": player1,
            "player2": player2,
            "season": season
        }
    )

    if response.status_code == 200:
        return response.json()

    return None

def get_league_market_values(
    league_id: int
):

    print("SERVICE CALLED WITH:", league_id)

    response = requests.get(
        f"{API_URL}/leagues/{league_id}/market-values"
    )

    print("SERVICE RESPONSE:", response.text)

    if response.status_code == 200:
        return response.json()

    return []

def get_league(
    league_id: int,
    season: str
):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return None

def get_average_age_by_club(
    league_id: int
):

    response = requests.get(
        f"{API_URL}/leagues/{league_id}/average-age"
    )

    if response.status_code == 200:

        return response.json()

    return []

def get_league_top_scorers(
    league_id: int,
    season: str
):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}/top-scorers",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_league_top_assists(
    league_id: int,
    season: str
):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}/top-assists",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_most_offensive_clubs(

    league_id: int,
    season: str

):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}/most-offensive",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_most_creative_clubs(

    league_id: int,
    season: str

):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}/most-creative",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_attack_scatter(

    league_id: int,
    season: str

):

    response = requests.get(

        f"{API_URL}/leagues/{league_id}/attack-scatter",

        params={

            "season": season

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_most_valuable_players(
    limit: int = 20,
    club: str = "All"
):

    response = requests.get(

        f"{API_URL}/players/most-valuable",

        params={
            "limit": limit,
            "club": club
        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_top_scorers(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All",

):

    response = requests.get(

        f"{API_URL}/players/rankings/top-scorers",

        params={

            "season": season,

            "limit": limit,

            "position": position,

            "min_minutes": min_minutes,

            "club": club,

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_top_assists(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):

    response = requests.get(

        f"{API_URL}/players/rankings/top-assists",

        params={

            "season": season,

            "limit": limit,

            "position": position,

            "min_minutes": min_minutes,

            "club": club,

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_top_goals_per90(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):

    response = requests.get(

        f"{API_URL}/players/rankings/top-goals-per90",

        params={

            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_top_contributions_per90(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):

    response = requests.get(

        f"{API_URL}/players/rankings/top-contributions-per90",

        params={

            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,

        }

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_summary():

    response = requests.get(

        f"{API_URL}/dashboard/summary"

    )

    if response.status_code == 200:

        return response.json()

    return {}

def get_dashboard_market_value_by_club():

    response = requests.get(

        f"{API_URL}/dashboard/market-value-by-club"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_position_distribution():

    response = requests.get(

        f"{API_URL}/dashboard/position-distribution"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_average_age_by_club():

    response = requests.get(

        f"{API_URL}/dashboard/average-age-by-club"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_top_nationalities():

    response = requests.get(

        f"{API_URL}/dashboard/top-nationalities"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_average_market_value_position():

    response = requests.get(

        f"{API_URL}/dashboard/average-market-value-position"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_top_scoring_clubs():

    response = requests.get(

        f"{API_URL}/dashboard/top-scoring-clubs"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_dashboard_top_assist_clubs():

    response = requests.get(

        f"{API_URL}/dashboard/top-assist-clubs"

    )

    if response.status_code == 200:

        return response.json()

    return []

def get_global_search(
    query: str
):

    response = requests.get(

        f"{API_URL}/search",

        params={
            "q": query
        }

    )

    if response.status_code == 200:

        return response.json()

    return {

        "players": [],

        "clubs": [],

        "leagues": []

    }



