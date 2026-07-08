import streamlit as st


def display_league_kpis(league):

    st.subheader("League Overview")

    c1, c2, c3 = st.columns(3)

    c4, c5, c6 = st.columns(3)

    c1.metric(
        "Clubs",
        league["clubs"]
    )

    c2.metric(
        "Players",
        league["players"]
    )

    c3.metric(
        "Market Value",
        f'{league["total_market_value"]/1_000_000_000:.2f} B€'
    )

    c4.metric(
        "Average Age",
        f'{league["average_age"]:.1f}'
    )

    c5.metric(
        "Goals",
        league["goals"]
    )

    c6.metric(
        "Assists",
        league["assists"]
    )