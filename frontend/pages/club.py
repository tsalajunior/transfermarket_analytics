import streamlit as st

from components.club_cards import (
    display_club_header,
    display_top_players
)
from components.player_tables import display_players_table
from components.charts import (
    display_market_value_chart,
    display_positions_chart
)
from components.club_kpis import display_club_kpis
from components.global_search import display_global_search

from services import (
    get_clubs,
    get_club,
    get_seasons,
    get_players_by_club
)

st.set_page_config(
    page_title="Club Dashboard",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Transfermarket | Club Dashboard")
display_global_search()

clubs = get_clubs()
seasons = get_seasons()

if not clubs:
    st.error("Impossible de récupérer les clubs.")
    st.stop()

selected_club_id = st.session_state.pop(
    "selected_club_id",
    None
)

default_index = 0

if selected_club_id is not None:

    for index, club in enumerate(clubs):

        if club["id"] == selected_club_id:

            default_index = index
            break

col1, col2 = st.columns([1, 3])

with col1:

    season = st.selectbox(
        "Season",
        seasons
    )

with col2:

    selected_club = st.selectbox(
        "Club",
        clubs,
        index=default_index,
        format_func=lambda club: club["name"]
    )

club = get_club(
    selected_club["id"],
    season
)

if club is None:

    st.error("Unable to retrieve the club information.")
    st.stop()

players = get_players_by_club(
    selected_club["id"],
    season
) or []

display_club_header(club)
display_club_kpis(club)
display_top_players(club)
display_players_table(players)

st.subheader("Squad Analytics")

col1, col2 = st.columns(2)

with col1:
    display_market_value_chart(players)

with col2:
    display_positions_chart(players)

