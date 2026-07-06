import pandas as pd
import plotly.express as px
import streamlit as st


def display_market_value_chart(players):

    if not players:
        return

    dataframe = pd.DataFrame(players)

    if "market_value_eur" not in dataframe.columns:
        return

    dataframe = dataframe.sort_values(
        by="market_value_eur",
        ascending=False
    )

    figure = px.bar(
        dataframe,
        x="market_value_eur",
        y="name",
        orientation="h",
        title="Market Value by Player",
        labels={
            "market_value_eur": "Market Value (€)",
            "name": "Player"
        }
    )

    figure.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=700
    )

    dataframe["market_value_m"] = (
        dataframe["market_value_eur"] / 1_000_000
    )

    figure = px.bar(
        dataframe,
        x="market_value_m",
        y="name",
        orientation="h",
        title="Market Value by Player",
        labels={
            "market_value_m": "Market Value (M€)",
            "name": "Player"
        }
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
        key="market_value_chart"
    )

def display_positions_chart(players):

    if not players:
        return

    dataframe = pd.DataFrame(players)

    if "position" not in dataframe.columns:
        return

    # -----------------------
    # Regroupement des postes
    # -----------------------

    def simplify_position(position):

        if position is None:
            return "Unknown"

        position = position.lower()

        # Gardiens
        if "goalkeeper" in position:
            return "Goalkeepers"

        # Défenseurs
        if (
            "back" in position
            or "centre-back" in position
            or "defender" in position
        ):
            return "Defenders"

        # Milieux
        if "midfield" in position:
            return "Midfielders"

        # Attaquants
        if (
            "winger" in position
            or "forward" in position
            or "striker" in position
            or "centre-forward" in position
            or "second striker" in position
            or "attack" in position
        ):
            return "Forwards"

        return "Other"

    dataframe["Role"] = dataframe["position"].apply(simplify_position)

    roles = (
        dataframe["Role"]
        .value_counts()
        .reset_index()
    )

    roles.columns = [
        "Role",
        "Players"
    ]

    # -----------------------
    # Couleurs
    # -----------------------

    colors = {
        "Goalkeepers": "#8e44ad",
        "Defenders": "#3498db",
        "Midfielders": "#2ecc71",
        "Forwards": "#e67e22",
        "Other": "#95a5a6"
    }

    figure = px.pie(
        roles,
        names="Role",
        values="Players",
        hole=0.45,
        color="Role",
        color_discrete_map=colors,
        title="Squad Composition"
    )

    figure.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    figure.update_layout(
        legend_title="Position",
        height=500
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
        key="positions_chart"
    )

