import pandas as pd
import streamlit as st
from utils.formatters import format_market_value
from utils.position_colors import color_position

def display_market_value_table(data):

    dataframe = pd.DataFrame(data)

    if dataframe.empty:

        st.info("No data available.")

        return

    dataframe = dataframe.rename(

        columns={

            "player": "Player",

            "club": "Club",

            "position": "Position",

            "market_value": "Market Value (€)"

        }

    )

    dataframe["Market Value (€)"] = dataframe[
        "Market Value (€)"
    ].apply(format_market_value)

    dataframe.insert(

        0,

        "#",

        range(1, len(dataframe) + 1)

    )

    podium = []

    for rank in dataframe["#"]:

        if rank == 1:
            podium.append("🥇")

        elif rank == 2:
            podium.append("🥈")

        elif rank == 3:
            podium.append("🥉")

        else:
            podium.append(str(rank))

    dataframe["#"] = podium

    styled = dataframe.style.map(
        color_position,
        subset=["Position"]
    )

    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True
    )

    # st.dataframe(

    #     dataframe[
    #         [
    #             "#",
    #             "Player",
    #             "Club",
    #             "Position",
    #             "Market Value (€)"
    #         ]
    #     ],

    #     hide_index=True,

    #     use_container_width=True

    # )

def display_top_scorers_table(data):

    dataframe = pd.DataFrame(data)
    dataframe.insert(
        0,
        "#",
        range(1, len(dataframe) + 1)
    )

    podium = []

    for rank in dataframe["#"]:

        if rank == 1:
            podium.append("🥇")

        elif rank == 2:
            podium.append("🥈")

        elif rank == 3:
            podium.append("🥉")

        else:
            podium.append(str(rank))

    dataframe["#"] = podium

    if dataframe.empty:

        st.info("No data available.")

        return

    dataframe = dataframe.rename(

        columns={

            "player": "Player",

            "club": "Club",

            "position": "Position",

            "goals": "Goals",

            "assists": "Assists",

            "minutes": "Minutes"

        }

    )

    styled = dataframe.style.map(
        color_position,
        subset=["Position"]
    )

    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True
    )

def display_top_assists_table(data):

    dataframe = pd.DataFrame(data)
    dataframe.insert(
        0,
        "#",
        range(1, len(dataframe) + 1)
    )

    podium = []

    for rank in dataframe["#"]:

        if rank == 1:
            podium.append("🥇")

        elif rank == 2:
            podium.append("🥈")

        elif rank == 3:
            podium.append("🥉")

        else:
            podium.append(str(rank))

    dataframe["#"] = podium

    if dataframe.empty:

        st.info("No data available.")

        return

    dataframe = dataframe.rename(

        columns={

            "player": "Player",

            "club": "Club",

            "position": "Position",

            "assists": "Assists",

            "goals": "Goals",

            "minutes": "Minutes"

        }

    )

    styled = dataframe.style.map(
        color_position,
        subset=["Position"]
    )

    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True
    )

def display_goals_per90_table(data):

    dataframe = pd.DataFrame(data)
    dataframe.insert(
        0,
        "#",
        range(1, len(dataframe) + 1)
    )

    podium = []

    for rank in dataframe["#"]:

        if rank == 1:
            podium.append("🥇")

        elif rank == 2:
            podium.append("🥈")

        elif rank == 3:
            podium.append("🥉")

        else:
            podium.append(str(rank))

    dataframe["#"] = podium

    if dataframe.empty:

        st.info("No data available.")

        return

    dataframe = dataframe.rename(

        columns={

            "player": "Player",

            "club": "Club",

            "position": "Position",

            "goals_per_90": "Goals /90",

            "goals": "Goals",

            "minutes": "Minutes"

        }

    )

    dataframe["Goals /90"] = dataframe["Goals /90"].round(2)

    styled = dataframe.style.map(
        color_position,
        subset=["Position"]
    )

    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True
    )

def display_contributions_per90_table(data):

    dataframe = pd.DataFrame(data)
    dataframe.insert(
        0,
        "#",
        range(1, len(dataframe) + 1)
    )

    podium = []

    for rank in dataframe["#"]:

        if rank == 1:
            podium.append("🥇")

        elif rank == 2:
            podium.append("🥈")

        elif rank == 3:
            podium.append("🥉")

        else:
            podium.append(str(rank))

    dataframe["#"] = podium

    if dataframe.empty:

        st.info("No data available.")

        return

    dataframe = dataframe.rename(

        columns={

            "player": "Player",

            "club": "Club",

            "position": "Position",

            "goal_contribution_per_90": "G+A /90",

            "goals": "Goals",

            "assists": "Assists"

        }

    )

    dataframe["G+A /90"] = dataframe["G+A /90"].round(2)

    styled = dataframe.style.map(
        color_position,
        subset=["Position"]
    )

    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True
    )

