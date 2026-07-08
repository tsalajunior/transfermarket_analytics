import streamlit as st


def _market_value(value):

    if value is None:
        return "-"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f} M€"

    return f"{value:,.0f} €"


def display_comparison_cards(comparison):

    player1 = comparison["player1"]
    player2 = comparison["player2"]

    st.subheader("Players")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"### {player1['name']}")

        st.metric(
            "Club",
            player1["club"]
            if player1["club"]
            else "-"
        )

        st.metric(
            "Nationality",
            player1["nationality"]
        )

        st.metric(
            "Position",
            player1["position"]
        )

        st.metric(
            "Market Value",
            _market_value(player1["market_value_eur"])
        )

    with col2:

        st.markdown(f"### {player2['name']}")

        st.metric(
            "Club",
            player2["club"]
            if player2["club"]
            else "-"
        )

        st.metric(
            "Nationality",
            player2["nationality"]
        )

        st.metric(
            "Position",
            player2["position"]
        )

        st.metric(
            "Market Value",
            _market_value(player2["market_value_eur"])
        )