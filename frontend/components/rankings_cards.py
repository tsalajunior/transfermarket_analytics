import streamlit as st


def display_rankings_cards(

    top_scorers,
    top_assists,
    most_valuable

):

    scorer = top_scorers[0] if top_scorers else None
    assister = top_assists[0] if top_assists else None
    valuable = most_valuable[0] if most_valuable else None

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "🥇 Top Scorer",

            scorer["player"],

            f'{scorer["goals"]} goals'

        )

    with col2:

        st.metric(

            "🎯 Top Assister",

            assister["player"],

            f'{assister["assists"]} assists'

        )

    with col3:

        st.metric(

            "💰 Most Valuable",

            valuable["player"],

            f'{valuable["market_value"]/1_000_000:.1f} M€'

        )