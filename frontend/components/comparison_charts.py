import plotly.graph_objects as go
import streamlit as st


def display_comparison_radar(comparison):

    player1 = comparison["player1"]
    player2 = comparison["player2"]

    categories = [
        "Goals",
        "Assists",
        "Appearances",
        "Minutes",
        "Goals /90",
        "Assists /90",
        "G+A /90"
    ]

    values1 = [
        player1["goals"],
        player1["assists"],
        player1["appearances"],
        player1["minutes_played"] / 100,
        player1["goals_per_90"] * 20,
        player1["assists_per_90"] * 20,
        player1["goal_contribution_per_90"] * 20
    ]

    values2 = [
        player2["goals"],
        player2["assists"],
        player2["appearances"],
        player2["minutes_played"] / 100,
        player2["goals_per_90"] * 20,
        player2["assists_per_90"] * 20,
        player2["goal_contribution_per_90"] * 20
    ]

    categories_closed = categories + [categories[0]]

    values1_closed = values1 + [values1[0]]
    values2_closed = values2 + [values2[0]]

    figure = go.Figure()

    figure.add_trace(

        go.Scatterpolar(

            r=values1_closed,

            theta=categories_closed,

            fill="toself",

            name=player1["name"],

            line=dict(
                color="#2563eb",
                width=3
            ),

            fillcolor="rgba(37,99,235,0.30)"
        )

    )

    figure.add_trace(

        go.Scatterpolar(

            r=values2_closed,

            theta=categories_closed,

            fill="toself",

            name=player2["name"],

            line=dict(
                color="#dc2626",
                width=3
            ),

            fillcolor="rgba(220,38,38,0.30)"
        )

    )

    figure.update_layout(

        title=dict(
            text="Performance Radar",
            x=0.5,
            xanchor="center",
            font=dict(size=22)
        ),

        polar=dict(

            bgcolor="white",

            radialaxis=dict(

                visible=True,

                showline=False,

                gridcolor="#E5E7EB",

                tickfont=dict(size=10)

            ),

            angularaxis=dict(

                gridcolor="#E5E7EB",

                tickfont=dict(size=12)

            )

        ),

        legend=dict(

            orientation="h",

            y=-0.10,

            x=0.5,

            xanchor="center"

        ),

        margin=dict(
            l=40,
            r=40,
            t=120,
            b=40
        ),

        height=700

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        config={
            "displayModeBar": False
        },

        key="comparison_radar"

    )

import plotly.graph_objects as go


def display_comparison_bar_charts(comparison):

    player1 = comparison["player1"]
    player2 = comparison["player2"]

    metrics = [

        ("Goals", player1["goals"], player2["goals"]),

        ("Assists", player1["assists"], player2["assists"]),

        (
            "Goals /90",
            player1["goals_per_90"],
            player2["goals_per_90"]
        ),

        (
            "Assists /90",
            player1["assists_per_90"],
            player2["assists_per_90"]
        ),

        (
            "G+A /90",
            player1["goal_contribution_per_90"],
            player2["goal_contribution_per_90"]
        ),

        (
            "Minutes",
            player1["minutes_played"],
            player2["minutes_played"]
        )

    ]

    st.subheader("Head-to-Head Performance")

    for title, value1, value2 in metrics:

        if value1 >= value2:

            colors = ["#16A34A", "#D1D5DB"]

        else:

            colors = ["#D1D5DB", "#16A34A"]

        figure = go.Figure()

        figure.add_trace(

            go.Bar(

                y=[
                    player1["name"],
                    player2["name"]
                ],

                x=[
                    value1,
                    value2
                ],

                orientation="h",

                text=[
                    value1,
                    value2
                ],

                textposition="outside",

                marker_color=colors

            )

        )

        figure.update_layout(

            title=title,

            height=250,

            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),

            showlegend=False,

            xaxis=dict(

                showgrid=True,

                gridcolor="#ECECEC"

            ),

            yaxis=dict(

                showgrid=False

            )

        )

        st.plotly_chart(

            figure,

            use_container_width=True,

            config={
                "displayModeBar": False
            },

            key=f"comparison_{title}"

        )