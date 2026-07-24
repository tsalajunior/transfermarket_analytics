import streamlit as st
from utils.formatters import format_market_value

def display_rankings_cards(

    top_scorers,
    top_assists,
    most_valuable,
    goals_per90,
    contributions_per90

):

    scorer = top_scorers[0] if top_scorers else {}
    assister = top_assists[0] if top_assists else {}
    valuable = most_valuable[0] if most_valuable else {}
    goals90 = goals_per90[0] if goals_per90 else {}
    contrib90 = contributions_per90[0] if contributions_per90 else {}

    # ==========================
    # Ligne 1
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Top Scorer",

            scorer.get("player", "—"),

            f'{scorer.get("goals",0)} goals'

        )

    with col2:

        st.metric(

            "Top Assister",

            assister.get("player", "—"),

            f'{assister.get("assists",0)} assists'

        )

    with col3:

        st.metric(

            "Most Valuable",

            valuable.get("player", "—"),

            format_market_value(

                valuable["market_value"]

            )

        )

    st.markdown("")

    # ==========================
    # Ligne 2
    # ==========================

    col4, col5 = st.columns(2)

    with col4:

        st.metric(

            "Goals /90",

            goals90.get("player", "—"),

            f'{goals90.get("goals_per_90",0):.2f}'

        )

    with col5:

        st.metric(

            "Goal Contributions /90",

            contrib90.get("player", "—"),

            f'{contrib90.get("goal_contribution_per_90",0):.2f}'

        )