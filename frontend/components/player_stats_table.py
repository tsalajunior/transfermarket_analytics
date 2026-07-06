import pandas as pd
import streamlit as st


def display_player_stats(player):

    stats = player["stats"]

    if not stats:
        st.warning("No statistics available.")
        return

    dataframe = pd.DataFrame(
        [
            ("Appearances", stats["appearances"]),
            ("Goals", stats["goals"]),
            ("Assists", stats["assists"]),
            ("Minutes Played", stats["minutes_played"]),
            ("Goals /90", stats["goals_per_90"]),
            ("Assists /90", stats["assists_per_90"]),
            ("Goal Contribution /90", stats["goal_contribution_per_90"]),
        ],
        columns=["Statistic", "Value"]
    )

    st.subheader("Detailed Statistics")

    st.dataframe(
        dataframe,
        hide_index=True,
        use_container_width=True
    )