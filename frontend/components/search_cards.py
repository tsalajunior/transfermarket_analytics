import streamlit as st


def display_search_cards(results):

    players = results["players"]
    clubs = results["clubs"]
    leagues = results["leagues"]

    if players:

        st.subheader("Players")

        for player in players:

            with st.container(border=True):

                col1, col2 = st.columns([5, 1])

                with col1:

                    st.markdown(
                        f"### {player['name']}"
                    )

                    st.caption(
                        f"{player['club']}"
                    )

                with col2:

                    if st.button(

                        "Open",

                        key=f"player_{player['id']}"

                    ):
                        st.session_state["player_id"] = player["id"]
                        st.switch_page("pages/Players.py")

    if clubs:

        st.subheader("Clubs")

        for club in clubs:

            with st.container(border=True):

                col1, col2 = st.columns([5, 1])

                with col1:

                    st.markdown(
                        f"### {club['name']}"
                    )

                with col2:

                    st.button(

                        "Open",

                        key=f"club_{club['id']}"

                    )

    if leagues:

        st.subheader("Leagues")

        for league in leagues:

            with st.container(border=True):

                col1, col2 = st.columns([5, 1])

                with col1:

                    st.markdown(
                        f"### {league['name']}"
                    )

                with col2:

                    st.button(

                        "Open",

                        key=f"league_{league['id']}"

                    )