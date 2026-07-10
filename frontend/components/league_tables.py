import pandas as pd
import streamlit as st


def display_top_scorers_table(players):

    dataframe = pd.DataFrame(players)

    if dataframe.empty:
        st.warning("No scorer data available.")
        return

    dataframe = dataframe.rename(
        columns={
            "player": "Player",
            "club": "Club",
            "goals": "Goals"
        }
    )

    st.subheader("Top Scorers")

    st.data_editor(

        dataframe[["Player", "Club", "Goals"]],

        use_container_width=True,

        hide_index=True,

        disabled=True

    )


def display_top_assists_table(players):

    dataframe = pd.DataFrame(players)

    if dataframe.empty:
        st.warning("No assist data available.")
        return

    dataframe = dataframe.rename(
        columns={
            "player": "Player",
            "club": "Club",
            "assists": "Assists"
        }
    )

    

    st.subheader("Top Assists")

    st.data_editor(

        dataframe[["Player", "Club", "Assists"]],

        use_container_width=True,

        hide_index=True,

        disabled=True

    )