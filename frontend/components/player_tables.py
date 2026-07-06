import pandas as pd
import streamlit as st


def display_players_table(players):

    st.subheader("Squad")

    if not players:
        st.warning("No players available.")
        return
    
    # 1️⃣ Création du DataFrame
    dataframe = pd.DataFrame(players)
    
    # 2️⃣ Renommage des colonnes
    dataframe = dataframe.rename(
        columns={
            "name": "Player",
            "position": "Position",
            "age": "Age",
            "market_value_eur": "Market Value (€)",
            "goals": "Goals",
            "assists": "Assists",
            "goals_per_90": "Goals /90",
            "assists_per_90": "Assists /90",
            "goal_contribution_per_90": "G+A /90"
        }
    )

     # 3️⃣ Tri
    dataframe = dataframe.sort_values(
        by="Market Value (€)",
        ascending=False
    )

    # ----------------------------
    # Filtres
    # ----------------------------

    col1, col2 = st.columns([2, 1])

    with col1:
        search = st.text_input(
            "Search player",
            placeholder="Type a player's name...",
            key="club_search_player"
        )

    with col2:

        positions = ["All"] + sorted(
            dataframe["Position"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_position = st.selectbox(
            "Position",
            positions,
            key="club_position_filter"
        )

    # ----------------------------
    # Recherche
    # ----------------------------

    if search:

        dataframe = dataframe[
            dataframe["Player"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # ----------------------------
    # Filtre poste
    # ----------------------------

    if selected_position != "All":

        dataframe = dataframe[
            dataframe["Position"] == selected_position
        ]

    # ----------------------------
    # Valeur
    # ----------------------------

    if "Market Value (€)" in dataframe.columns:

        dataframe["Market Value (€)"] = (

            dataframe["Market Value (€)"]

            .fillna(0)

            .astype(int)

            .map(lambda x:
                f"{x/1_000_000:.0f} M€"
                if x % 1_000_000 == 0
                else f"{x/1_000_000:.1f} M€"
            )

        )

    st.caption(
        f"{len(dataframe)} players found"
    )

    st.data_editor(
        dataframe,
        use_container_width=True,
        hide_index=True,
        disabled=True,
        column_config={
            "Player": st.column_config.TextColumn(
                "Player",
                width="medium"
            ),

            "Position": st.column_config.TextColumn(
                "Position",
                width="medium"
            ),

            "Age": st.column_config.NumberColumn(
                "Age",
                format="%d"
            ),

            "Market Value (€)": st.column_config.TextColumn(
                "Market Value (€)",
                width="medium"
            ),

            "Goals": st.column_config.NumberColumn(
                "Goals"
            ),

            "Assists": st.column_config.NumberColumn(
                "Assists"
            ),

            "Goals /90": st.column_config.NumberColumn(
                "Goals /90",
                format="%.2f"
            ),

            "Assists /90": st.column_config.NumberColumn(
                "Assists /90",
                format="%.2f"
            ),

            "G+A /90": st.column_config.NumberColumn(
                "G+A /90",
                format="%.2f"
            )
        }
    )