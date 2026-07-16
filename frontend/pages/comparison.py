import streamlit as st

from services import (
    get_players,
    get_seasons,
    compare_players
)

from components.comparison_cards import (
    display_comparison_cards
)
from components.comparison_kpis import display_comparison_kpis
from components.comparison_charts import (
    display_comparison_radar,
    display_comparison_bar_charts
)
from components.comparison_table import display_comparison_table
from components.global_search import display_global_search


st.set_page_config(
    page_title="Player Comparison",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ Transfermarket | Player Comparison")
display_global_search()

# -----------------------
# Chargement des données
# -----------------------

players = get_players()

if not players:

    st.error("Impossible de récupérer les joueurs.")

    st.stop()

seasons = get_seasons()

# -----------------------
# Sélection
# -----------------------

col1, col2, col3 = st.columns([1, 2, 2])

with col1:

    season = st.selectbox(
        "Season",
        seasons
    )

with col2:

    player1 = st.selectbox(
        "Player A",
        players,
        format_func=lambda p: f'{p["name"]} — {p["club"]}'
    )

with col3:

    player2 = st.selectbox(
        "Player B",
        players,
        format_func=lambda p: f'{p["name"]} — {p["club"]}'
    )

# Empêcher la comparaison du même joueur

if player1["id"] == player2["id"]:

    st.warning("Please select two different players.")

    st.stop()

# -----------------------
# Comparaison
# -----------------------

comparison = compare_players(
    player1["id"],
    player2["id"],
    season
)

if comparison is None:

    st.error("Unable to compare these players.")

    st.stop()

# -----------------------
# Affichage
# -----------------------

display_comparison_cards(comparison)
display_comparison_kpis(comparison)
display_comparison_radar(comparison)
display_comparison_bar_charts(comparison)
st.divider()

display_comparison_table(comparison)