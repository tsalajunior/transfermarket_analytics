import streamlit as st

from services import (
    get_top_scorers,
    get_top_assists,
    get_top_goals_per90,
    get_top_contributions_per90,
    get_most_valuable_players
)

from components.rankings_filters import display_rankings_filters
from components.rankings_cards import display_rankings_cards

from components.rankings_tables import (
    display_market_value_table,
    display_top_scorers_table,
    display_top_assists_table,
    display_goals_per90_table,
    display_contributions_per90_table
)
from components.global_search import display_global_search


st.set_page_config(
    page_title="Rankings",
    page_icon="⚽",
    layout="wide"
)
st.title("Transfermarket | Rankings")
display_global_search()

filters = display_rankings_filters()

# -----------------------------
# Data
# -----------------------------

top_scorers = get_top_scorers(
    season=filters["season"],
    limit=filters["limit"],
    position=filters["position"],
    club=filters["club"],
    min_minutes=filters["min_minutes"]
)

top_assists = get_top_assists(
    season=filters["season"],
    limit=filters["limit"],
    position=filters["position"],
    club=filters["club"],
    min_minutes=filters["min_minutes"]
)

goals_per90 = get_top_goals_per90(
    season=filters["season"],
    limit=filters["limit"],
    position=filters["position"],
    club=filters["club"],
    min_minutes=filters["min_minutes"]
)

contributions_per90 = get_top_contributions_per90(
    season=filters["season"],
    limit=filters["limit"],
    position=filters["position"],
    club=filters["club"],
    min_minutes=filters["min_minutes"]
)

most_valuable = get_most_valuable_players(
    limit=filters["limit"],
    club=filters["club"]
)

# -----------------------------
# Cards
# -----------------------------

display_rankings_cards(
    top_scorers,
    top_assists,
    most_valuable,
    goals_per90,
    contributions_per90
)

# -----------------------------
# Tabs
# -----------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Market Value",
        "Top Scorers",
        "Top Assists",
        "Goals /90",
        "Goal Contributions /90",
    ]
)

with tab1:
    display_market_value_table(most_valuable)

with tab2:
    display_top_scorers_table(top_scorers)

with tab3:
    display_top_assists_table(top_assists)

with tab4:
    display_goals_per90_table(goals_per90)

with tab5:
    display_contributions_per90_table(contributions_per90)