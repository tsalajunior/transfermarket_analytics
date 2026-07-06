import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ======================================================
# Offensive contribution
# ======================================================

def display_offensive_chart(player):

    stats = player["stats"]

    if not stats:
        return

    figure = px.pie(
        names=[
            "Goals",
            "Assists"
        ],
        values=[
            stats["goals"],
            stats["assists"]
        ],
        title="Offensive Contribution"
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
        key="player_offensive_chart"
    )


# ======================================================
# Per 90 metrics
# ======================================================

def display_per90_chart(player):

    stats = player["stats"]

    if not stats:
        return

    metrics = {
        "Goals /90": stats["goals_per_90"],
        "Assists /90": stats["assists_per_90"],
        "G+A /90": stats["goal_contribution_per_90"]
    }

    figure = px.bar(
        x=list(metrics.values()),
        y=list(metrics.keys()),
        orientation="h",
        text=list(metrics.values()),
        title="Production per 90 Minutes"
    )

    figure.update_traces(

        texttemplate="%{text:.2f}",

        textposition="outside",

        cliponaxis=False

    )

    figure.update_layout(

        xaxis_title="Per 90",

        yaxis_title="",

        showlegend=False,

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    st.plotly_chart(
        figure,
        use_container_width=True,
        key="player_per90_chart"
    )

# ======================================================
# Minutes played gauge
# ======================================================

def display_minutes_gauge(player):

    stats = player["stats"]

    if not stats:
        return

    minutes = stats["minutes_played"]

    figure = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=minutes,

            title={
                "text": "Minutes Played"
            },

            gauge={

                "axis": {
                    "range": [0, 3500]
                },

                "bar": {
                    "thickness": 0.5
                }

            }

        )

    )

    st.plotly_chart(
        figure,
        use_container_width=True,
        key="player_minutes_gauge"
    )