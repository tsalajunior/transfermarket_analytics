import pandas as pd
import streamlit as st


def display_comparison_table(comparison):

    player1 = comparison["player1"]
    player2 = comparison["player2"]

    dataframe = pd.DataFrame({

        "Statistic": [

            "Age",
            "Position",
            "Appearances",
            "Minutes",
            "Goals",
            "Assists",
            "Goals /90",
            "Assists /90",
            "G+A /90",
            "Market Value (€)"

        ],

        player1["name"]: [

            player1.get("age"),
            player1.get("position"),
            player1.get("appearances"),
            player1.get("minutes_played"),
            player1.get("goals"),
            player1.get("assists"),
            round(player1.get("goals_per_90", 0), 2),
            round(player1.get("assists_per_90", 0), 2),
            round(player1.get("goal_contribution_per_90", 0), 2),
            f'{player1.get("market_value_eur",0):,.0f} €'

        ],

        player2["name"]: [

            player2.get("age"),
            player2.get("position"),
            player2.get("appearances"),
            player2.get("minutes_played"),
            player2.get("goals"),
            player2.get("assists"),
            round(player2.get("goals_per_90", 0), 2),
            round(player2.get("assists_per_90", 0), 2),
            round(player2.get("goal_contribution_per_90", 0), 2),
            f'{player2.get("market_value_eur",0):,.0f} €'

        ]

    })

    st.subheader("Detailed Statistics")

    st.data_editor(

        dataframe,

        use_container_width=True,

        hide_index=True,

        disabled=True,

        column_config={

            "Statistic": st.column_config.TextColumn(
                "Statistic",
                width="medium"
            )

        }

    )