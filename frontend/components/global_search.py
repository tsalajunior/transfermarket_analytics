import streamlit as st

from api_services import get_global_search


def display_global_search():

    st.sidebar.markdown("## Global Search")

    query = st.sidebar.text_input(

        "Search player, club or league",

        placeholder="e.g. Dembélé..."

    )

    if not query:

        return

    results = get_global_search(query)

    players = results["players"]

    clubs = results["clubs"]

    # leagues = results["leagues"]

    if players:

        st.sidebar.markdown("### Players")

        for player in players:

            if st.sidebar.button(

                player["name"],

                key=f"player_{player['id']}"

            ):

                st.session_state["selected_player_id"] = player["id"]
                st.switch_page("pages/player.py")

    if clubs:

        st.sidebar.markdown("### Clubs")

        for club in clubs:

            if st.sidebar.button(

                club["name"],

                key=f"club_{club['id']}"

            ):

                st.session_state["selected_club_id"] = club["id"]
                st.switch_page("pages/club.py")

    # if leagues:

    #     st.sidebar.markdown("### Leagues")

    #     for league in leagues:

    #         if st.sidebar.button(

    #             league["name"],

    #             key=f"league_{league['id']}"

    #         ):

    #             st.session_state["selected_league_id"] = league["id"]
                st.switch_page("pages/league.py")

    if not players and not clubs :

        st.sidebar.info(

            "No results found."

        )

