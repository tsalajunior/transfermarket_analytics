import streamlit as st


def display_club_header(club: dict):

    st.header(club["name"])

    st.caption(
        f'{club["country"]} • {club["league"]}'
    )


def display_top_players(club: dict):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Meilleur buteur")

        scorer = club["top_scorer"]

        st.metric(
            scorer["name"],
            f"{scorer['goals']} buts"
        )

    with col2:

        st.subheader("Meilleur passeur")

        passer = club["top_assist"]

        st.metric(
            passer["name"],
            f"{passer['assists']} passes"
        )