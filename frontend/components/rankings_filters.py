import streamlit as st

from services import get_seasons


def display_rankings_filters():

    seasons = get_seasons()

    col1, col2, col3, col4 = st.columns(4)

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

        min_minutes = st.slider(
            "Minimum Minutes",
            min_value=0,
            max_value=3000,
            value=500,
            step=100
        )

    with col4:

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

        "min_minutes": min_minutes,

        "limit": limit

    }