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
from services import (
    get_clubs,
    get_club,
    get_seasons,
    get_players_by_club
)

st.title("⚽ Transfermarket | Club Dashboard")

# -----------------------
# Récupération des données
# -----------------------

clubs = get_clubs()

if not clubs:
    st.error("Impossible de récupérer les clubs.")
    st.stop()

seasons = get_seasons()

# -----------------------
# Choix de la saison
# -----------------------


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
        format_func=lambda club: club["name"]
    )


club = get_club(
    selected_club["id"],
    season
)
if club is None:

    st.error("Impossible de récupérer les informations du club.")

    st.stop()

players = (
    get_players_by_club(
        selected_club["id"],
        season
    )
    or []
)

# -----------------------
# Affichage
# -----------------------

if club:

    display_club_header(club)

    # st.write(club)
    display_club_kpis(club)

    display_top_players(club)

    display_players_table(players)

    st.subheader("Squad Analytics")

    col1, col2 = st.columns(2)

    with col1:
        display_market_value_chart(players)

    with col2:
        display_positions_chart(players)