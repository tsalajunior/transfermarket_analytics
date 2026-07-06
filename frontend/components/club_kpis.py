import streamlit as st


def kpi_card(title, value):

    with st.container(border=True):

        st.caption(title)

        st.markdown(
            f"<h2 style='text-align:center'>{value}</h2>",
            unsafe_allow_html=True
        )

def display_club_kpis(club):

    st.subheader("Club Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        kpi_card(
            "Squad",
            club["players_count"]
        )

        average_age = club.get("average_age")

        kpi_card(
            "Average Age",
            f"{average_age:.1f}"
            if average_age is not None
            else "-"
        )

    with col2:

        kpi_card(
            "Squad Value",
            f'{club["total_market_value"]/1_000_000:.1f} M€'
        )

        kpi_card(
            "Average Value",
            f'{club["average_market_value"]/1_000_000:.1f} M€'
        )

    with col3:

        kpi_card(
            "Goals",
            club["total_goals"]
        )

        kpi_card(
            "Assists",
            club["total_assists"]
        )