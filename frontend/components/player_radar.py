import plotly.graph_objects as go
import streamlit as st


def display_player_radar(player):

    stats = player["stats"]

    if not stats:
        st.warning("No statistics available.")
        return

    categories = [
        "Goals",
        "Assists",
        "Appearances",
        "Minutes",
        "Goals /90",
        "Assists /90",
        "G+A /90"
    ]

    values = [
        stats["goals"],
        stats["assists"],
        stats["appearances"],
        stats["minutes_played"] / 100,
        stats["goals_per_90"] * 20,
        stats["assists_per_90"] * 20,
        stats["goal_contribution_per_90"] * 20
    ]

    categories.append(categories[0])
    values.append(values[0])

    figure = go.Figure()

    figure.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            name=player["name"]

        )

    )

    figure.update_layout(

        title="Performance Radar",

        polar=dict(

            radialaxis=dict(

                visible=True

            )

        ),

        showlegend=False,

        height=600

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="player_radar"

    )