from api import api_get
import streamlit as st

@st.cache_data
def get_clubs():
    return api_get("/clubs")

@st.cache_data(ttl=300)
def get_club(
    club_id,
    season
):
 return api_get(
     f"/clubs/{club_id}",
     {
         "season": season
     }
 )

@st.cache_data
def get_seasons():
    return api_get("/leagues/seasons")

@st.cache_data
def get_players_by_club(
    club_id,
    season
):
    return api_get(
     f"/clubs/{club_id}/players",
     {
         "season": season
     }
 )

@st.cache_data
def search_players(query: str):

    return api_get(
        "/players/search",
        {"q": query}
    )

@st.cache_data
def get_players():
    return api_get("/players")

@st.cache_data(ttl=300)
def get_player(
    player_id: int,
    season: str
):
    return api_get(
        f"/players/{player_id}",
        {
            "season": season
        }
    )

@st.cache_data(ttl=300)
def compare_players(
    player1: int,
    player2: int,
    season: str
):
    return api_get(
        "/players/compare",
        {
            "player1": player1,
            "player2": player2,
            "season": season
        }
    ) 

@st.cache_data
def get_league_market_values(
    league_id: int
):
    return api_get(
        f"/leagues/{league_id}/market-values"
    )

@st.cache_data(ttl=300)
def get_league(
    league_id: int,
    season: str
):
    return api_get(
        f"/leagues/{league_id}",
        {
            "season": season
        }

    )

@st.cache_data
def get_average_age_by_club(
    league_id: int
):

    return api_get(
        f"/leagues/{league_id}/average-age"
    )

@st.cache_data
def get_league_top_scorers(
    league_id: int,
    season: str
):

    return api_get(

        f"/leagues/{league_id}/top-scorers",
        {
            "season": season
        }

    )

@st.cache_data
def get_league_top_assists(
    league_id: int,
    season: str
):

    return api_get(

        f"/leagues/{league_id}/top-assists",
        {
            "season": season
        }

    )

@st.cache_data
def get_most_offensive_clubs(

    league_id: int,
    season: str

):

    return api_get(
        f"/leagues/{league_id}/most-offensive",
        {
            "season": season
        }

    )

@st.cache_data
def get_most_creative_clubs(

    league_id: int,
    season: str

):
    return api_get(
        f"/leagues/{league_id}/most-creative",
        {
            "season": season
        }

    ) 

@st.cache_data
def get_attack_scatter(

    league_id: int,
    season: str

):
    return api_get(
        f"/leagues/{league_id}/attack-scatter",
        {
            "season": season
        }
    ) 

@st.cache_data
def get_most_valuable_players(
    limit: int = 20,
    club: str = "All"
):
    return api_get(
        "/players/most-valuable",
        {
            "limit": limit,
            "club": club
        }

    ) 

@st.cache_data
def get_top_scorers(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All",

):
    return api_get(
        "/players/rankings/top-scorers",
        {
            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,
        }

    ) 

@st.cache_data
def get_top_assists(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):
    return api_get(
        "/players/rankings/top-assists",
        {
            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,
        }

    ) 

@st.cache_data
def get_top_goals_per90(

    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):
    return api_get(
        "/players/rankings/top-goals-per90",
            {
            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,
        }

    ) 

@st.cache_data
def get_top_contributions_per90(
    season="25/26",
    limit=20,
    position="All",
    min_minutes=0,
    club: str = "All"

):

    return api_get(
        "/players/rankings/top-contributions-per90",
        {
            "season": season,
            "limit": limit,
            "position": position,
            "min_minutes": min_minutes,
            "club": club,

        }

    ) 

@st.cache_data(ttl=300)
def get_dashboard_summary():
    return api_get("/dashboard/summary") 


@st.cache_data(ttl=300)
def get_dashboard_market_value_by_club():
    return api_get("/dashboard/market-value-by-club") 


@st.cache_data(ttl=300)
def get_dashboard_position_distribution():
    return api_get("/dashboard/position-distribution") 


@st.cache_data(ttl=300)
def get_dashboard_average_age_by_club():
    return api_get("/dashboard/average-age-by-club") 


@st.cache_data(ttl=300)
def get_dashboard_top_nationalities():
    return api_get("/dashboard/top-nationalities") 


@st.cache_data(ttl=300)
def get_dashboard_average_market_value_position():
    return api_get("/dashboard/average-market-value-position") 


@st.cache_data(ttl=300)
def get_dashboard_top_scoring_clubs():
    return api_get("/dashboard/top-scoring-clubs") 


@st.cache_data(ttl=300)
def get_dashboard_top_assist_clubs():
    return api_get("/dashboard/top-assist-clubs") 


@st.cache_data(ttl=60)
def get_global_search(query):
    return api_get(
        "/search",
        {
            "q": query
        }
    ) or {
        "players": [],
        "clubs": [],
        "leagues": []
    }



