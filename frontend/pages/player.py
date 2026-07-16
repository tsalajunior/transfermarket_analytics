import streamlit as st
from services import (
    get_players,
    get_player,
    get_seasons
)
from components.player_card import display_player_card
from components.player_kpis import display_player_kpis
from components.player_stats_table import display_player_stats
from components.player_charts import (
    display_offensive_chart,
    display_per90_chart,
    display_minutes_gauge
)
from components.player_radar import display_player_radar
from components.global_search import display_global_search


st.set_page_config(
    page_title="Player Dashboard",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ Transfermarket | Player Dashboard")
display_global_search()


players = get_players()
if not players:
    st.error("Impossible de récupérer les joueurs.")
    st.stop()

seasons = get_seasons()

col1, col2 = st.columns([1, 3])
selected_player_id = st.session_state.pop(
    "selected_player_id",
    None
)

default_index = 0

if selected_player_id is not None:

    for index, player in enumerate(players):

        if player["id"] == selected_player_id:

            default_index = index

            break

with col1:
    season = st.selectbox(
        "Season",
        seasons
    )

with col2:
    selected_player = st.selectbox(
        "Player",
        players,
        index=default_index,
        format_func=lambda player: player["name"]
    )

player = get_player(
    selected_player["id"],
    season
)

if player is None:
    st.error("Impossible de récupérer les données du joueur.")
    st.stop()

display_player_card(player)
display_player_kpis(player)
display_player_stats(player)

st.subheader("Performance Visualisation")

col1, col2 = st.columns(2)

with col1:
    display_offensive_chart(player)

with col2:
    display_per90_chart(player)

display_minutes_gauge(player)

st.subheader("Performance Radar")
display_player_radar(player)