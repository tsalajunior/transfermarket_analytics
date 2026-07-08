import streamlit as st
import pandas as pd
from services import get_attack_scatter, get_average_age_by_club, get_most_creative_clubs
from services import (
    get_seasons,
    get_league,
    get_league_market_values
)

from components.league_kpis import display_league_kpis
from components.league_charts import (
    display_attack_scatter,
    display_market_values_chart,
    display_average_age_chart,
    display_most_creative_chart,
    display_top_scorers_chart,
    display_top_assists_chart,
    display_most_offensive_chart
)
from services import (
    get_league_top_scorers, 
    get_league_top_assists, 
    get_most_offensive_clubs
)

st.title("Ligue 1 Dashboard")

# -----------------------------
# Saison
# -----------------------------

seasons = get_seasons()

season = st.selectbox(
    "Season",
    seasons
)

# -----------------------------
# Dashboard
# -----------------------------

LEAGUE_ID = 2

league = get_league(
    LEAGUE_ID,
    season
)

if league is None:

    st.error("Unable to load league.")

    st.stop()

display_league_kpis(league)

# -----------------------------
# Graphique
# -----------------------------

market_values = get_league_market_values(LEAGUE_ID)
average_age = get_average_age_by_club(
    LEAGUE_ID
)
top_scorers = get_league_top_scorers(

    LEAGUE_ID,
    season

)

top_assists = get_league_top_assists(

    LEAGUE_ID,
    season

)
offensive = get_most_offensive_clubs(

    LEAGUE_ID,
    season

)

col1, col2 = st.columns(2)

with col1:
    display_market_values_chart(market_values)

with col2:
    display_average_age_chart(average_age)

col3, col4 = st.columns(2)

with col3:
    display_top_scorers_chart(top_scorers)

with col4:
    display_top_assists_chart(top_assists)

col5, col6 = st.columns(2)

with col5:
    display_most_offensive_chart(offensive)


creative = get_most_creative_clubs(
    LEAGUE_ID,
    season
)

display_most_creative_chart(
    creative
)

scatter = get_attack_scatter(
    LEAGUE_ID,
    season
)

display_attack_scatter(
    scatter
)