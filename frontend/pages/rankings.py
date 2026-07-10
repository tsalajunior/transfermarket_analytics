import streamlit as st

from services import (
    get_league_top_scorers,
    get_league_top_assists,
    get_most_valuable_players
)
from components.rankings_cards import display_rankings_cards
from components.rankings_filters import (
    display_rankings_filters
)

st.title("🏆 Rankings")

filters = display_rankings_filters()

top_scorers = get_league_top_scorers(
    season=filters["season"],
    limit=filters["limit"]
)

top_assists = get_league_top_assists(
    season=filters["season"],
    limit=filters["limit"]
)

most_valuable = get_most_valuable_players(
    filters["limit"]

)

display_rankings_cards(

    top_scorers,

    top_assists,

    market_values

)

display_rankings_cards(

    top_scorers,

    top_assists,

    most_valuable

)