import pandas as pd
import streamlit as st
from components.dashboard_charts import (
    display_average_age_by_club, 
    display_market_value_by_club, 
    display_position_distribution
)
from api_services import (
    get_dashboard_average_age_by_club,
    get_dashboard_summary, 
    get_dashboard_market_value_by_club,
    get_dashboard_position_distribution,
    get_dashboard_top_nationalities,
    get_dashboard_average_market_value_position,
    get_dashboard_top_scoring_clubs,
    get_dashboard_top_assist_clubs
)
from components.global_search import display_global_search

st.set_page_config(
    page_title="Transfermarket Analytics",
    page_icon="⚽",
    layout="wide"
)
st.title("Transfermarket Analytics | Dashboard")

with st.spinner("Loading dashboard..."):

    display_global_search()

    summary = get_dashboard_summary()
    charts = {
        "market_values" : get_dashboard_market_value_by_club(),
        "position_distribution" : get_dashboard_position_distribution(),
        "average_age" : get_dashboard_average_age_by_club(),
        "top_nationalities" : get_dashboard_top_nationalities(),
        "average_position_value" : get_dashboard_average_market_value_position(),
        "top_scoring_clubs" : get_dashboard_top_scoring_clubs(),
        "top_assist_clubs" : get_dashboard_top_assist_clubs()
    }

    display_market_value_by_club(
        (charts["market_values"])
    )
    display_position_distribution(
        (charts["position_distribution"])
    )
    display_average_age_by_club(
        (charts["average_age"])
    )

    st.subheader("Top 10 Nationalities")
    df = pd.DataFrame(charts["top_nationalities"])
    st.bar_chart(
        df.set_index("nationality")
    )

    st.subheader(
        "Average Market Value by Position"
    )
    df = pd.DataFrame(
        (charts["average_position_value"])
    )
    df["Average Value (M€)"] = (
        df["average_value"] / 1_000_000
    ).round(1)
    st.bar_chart(
        df.set_index("position")[
            "Average Value (M€)"
        ]
    )

    st.subheader(
        "Top 10 Highest Scoring Clubs"
    )
    df = pd.DataFrame(
        (charts["top_scoring_clubs"])
    )
    st.bar_chart(
        df.set_index("club")
    )

    st.subheader(
        "Top 10 Clubs with Most Assists"
    )
    df = pd.DataFrame(
        (charts["top_assist_clubs"])
    )
    st.bar_chart(
        df.set_index("club")
    )