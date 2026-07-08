import pandas as pd
import streamlit as st


def display_comparison_kpis(comparison):

    player1 = comparison["player1"]
    player2 = comparison["player2"]

    metrics = [

        ("Goals", player1["goals"], player2["goals"]),

        ("Assists", player1["assists"], player2["assists"]),

        ("Appearances", player1["appearances"], player2["appearances"]),

        ("Minutes", player1["minutes_played"], player2["minutes_played"]),

        ("Goals /90", player1["goals_per_90"], player2["goals_per_90"]),

        ("Assists /90", player1["assists_per_90"], player2["assists_per_90"]),

        (
            "G+A /90",
            player1["goal_contribution_per_90"],
            player2["goal_contribution_per_90"]
        ),

        (
            "Market Value (€)",
            player1["market_value_eur"],
            player2["market_value_eur"]
        )

    ]

    rows = []

    for metric, value1, value2 in metrics:

        if value1 > value2:

            winner = player1["name"]

        elif value2 > value1:

            winner = player2["name"]

        else:

            winner = "Draw"

        rows.append({

            "Metric": metric,

            player1["name"]: value1,

            player2["name"]: value2,

            "Winner": winner

        })

    dataframe = pd.DataFrame(rows)

    st.subheader("Head-to-Head Statistics")

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )