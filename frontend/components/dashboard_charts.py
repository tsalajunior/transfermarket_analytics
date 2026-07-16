import pandas as pd
import plotly.express as px
import streamlit as st


def display_market_value_by_club(data):

    dataframe = pd.DataFrame(data)

    fig = px.bar(

        dataframe,

        x="club",

        y="market_value",

        text="market_value",

        color="market_value",

        color_continuous_scale="Blues"

    )

    fig.update_traces(

        texttemplate="%{text:.2s}",

        textposition="outside"

    )

    fig.update_layout(

        title="Total Market Value by Club",

        xaxis_title="",

        yaxis_title="Market Value (€)",

        coloraxis_showscale=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

def display_position_distribution(data):

    dataframe = pd.DataFrame(data)

    fig = px.pie(

        dataframe,

        names="position",

        values="count",

        # The hole (hole=0.45) creates a donut chart, which looks more modern than a simple pie chart.
        hole=0.45,

        title="Player Position Distribution"

    )

    fig.update_traces(

        textinfo="percent+label"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

def display_average_age_by_club(data):

    dataframe = pd.DataFrame(data)

    fig = px.bar(

        dataframe,

        x="average_age",

        y="club",

        orientation="h",

        text="average_age",

        color="average_age",

        color_continuous_scale="Teal"

    )

    fig.update_layout(

        title="Average Age by Club",

        xaxis_title="Average Age",

        yaxis_title="",

        coloraxis_showscale=False

    )

    fig.update_traces(

        texttemplate="%{text:.1f}",

        textposition="outside"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


