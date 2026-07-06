import streamlit as st


def display_player_kpis(player):

    stats = player["stats"]

    if not stats:
        st.warning("No statistics available.")
        return

    st.subheader("Season Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Appearances",
        stats["appearances"]
    )

    col2.metric(
        "Goals",
        stats["goals"]
    )

    col3.metric(
        "Assists",
        stats["assists"]
    )

    col4.metric(
        "Minutes",
        stats["minutes_played"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Goals /90",
        stats["goals_per_90"]
    )

    col2.metric(
        "Assists /90",
        stats["assists_per_90"]
    )

    col3.metric(
        "G+A /90",
        stats["goal_contribution_per_90"]
    )