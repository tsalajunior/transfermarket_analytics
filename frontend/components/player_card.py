import streamlit as st


def display_player_card(player):

    st.header(player["name"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Club",
            player["club"]["name"]
            if player["club"]
            else "-"
        )

    with col2:
        st.metric(
            "Nationality",
            player["nationality"]
        )

    with col3:
        st.metric(
            "Position",
            player["position"]
        )

    with col4:
        market_value = player.get("market_value_eur")

        if market_value:

            value = (
                f"{market_value/1_000_000:.1f} M€"
            )

        else:
            value = "-"

        st.metric(
            "Market Value",
            value
        )