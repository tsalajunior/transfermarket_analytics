import streamlit as st
from components.global_search import display_global_search
from components.league_kpis import display_league_kpis
from components.league_charts import (
    display_market_values_chart,
    display_average_age_chart,
    display_top_scorers_chart,
    display_top_assists_chart,
    display_most_offensive_chart,
    display_most_creative_chart,
    display_attack_scatter
)
from components.league_tables import (
    display_top_scorers_table,
    display_top_assists_table
)

from api_services import (
    get_seasons,
    get_league,
    get_league_market_values,
    get_average_age_by_club,
    get_league_top_scorers,
    get_league_top_assists,
    get_most_offensive_clubs,
    get_most_creative_clubs,
    get_attack_scatter
)

st.set_page_config(
    page_title="Ligue 1 Dashboard",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ Transfermarket | Ligue 1 Dashboard")

with st.spinner("Loading League Dashboard..."):
    display_global_search()

    LEAGUE_ID = 2

    seasons = get_seasons()

    season = st.selectbox(
        "Season",
        seasons
    )

    league = get_league(
        LEAGUE_ID,
        season
    )

    if league is None:

        st.error("Unable to load league.")
        st.stop()

    display_league_kpis(league)

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

    creative = get_most_creative_clubs(
        LEAGUE_ID,
        season
    )

    scatter = get_attack_scatter(
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

    with col6:
        display_most_creative_chart(creative)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        display_top_scorers_table(top_scorers)

    with col2:
        display_top_assists_table(top_assists)

    display_attack_scatter(scatter)

