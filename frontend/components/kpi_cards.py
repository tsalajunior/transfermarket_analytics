import streamlit as st


def display_kpis(players):

    if not players:
        return

    total_value = sum(
        player.get("market_value_eur") or 0
        for player in players
    )

    total_goals = sum(
        player.get("goals") or 0
        for player in players
    )

    total_assists = sum(
        player.get("assists") or 0
        for player in players
    )

    ages = [
        player.get("age")
        for player in players
        if player.get("age") is not None
    ]

    average_age = (
        round(sum(ages) / len(ages), 1)
        if ages else "-"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Effectif",
        len(players)
    )

    col2.metric(
        "Valeur",
        f"{total_value/1_000_000:.1f} M€"
    )

    col3.metric(
        "Buts",
        total_goals
    )

    col4.metric(
        "Passes",
        total_assists
    )

    col5.metric(
        "Âge moyen",
        average_age
    )