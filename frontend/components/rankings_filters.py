import streamlit as st

from api_services import (
    get_seasons,
    get_clubs
)


def display_rankings_filters():

    seasons = get_seasons()
    clubs = get_clubs()

    club_options = ["All"] + [
        club["name"]
        for club in clubs
    ]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        season = st.selectbox(
            "Season",
            seasons,
            index=0
        )

    with col2:

        position = st.selectbox(
            "Position",
            [
                "All",
                "Goalkeeper",
                "Centre-Back",
                "Left-Back",
                "Right-Back",
                "Defensive Midfield",
                "Central Midfield",
                "Attacking Midfield",
                "Left Winger",
                "Right Winger",
                "Centre-Forward"
            ]
        )

    with col3:

        selected_club = st.selectbox(
            "Club",
            club_options
        )

    with col4:

        min_minutes = st.slider(
            "Minimum Minutes",
            min_value=0,
            max_value=3000,
            value=500,
            step=100
        )

    with col5:

        limit = st.selectbox(
            "Top",
            [
                10,
                20,
                30,
                50
            ],
            index=1
        )

    return {
        "season": season,
        "position": position,
        "club": selected_club,
        "min_minutes": min_minutes,
        "limit": limit
    }