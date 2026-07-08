import plotly.express as px
import pandas as pd
import streamlit as st


def display_market_values_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="market_value",

        y="club",

        orientation="h",

        text="market_value",

        color="market_value",

        color_continuous_scale="Blues"

    )

    figure.update_layout(

        title="Squad Market Value",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=700

    )

    figure.update_traces(

        texttemplate="%{text:.0s}",

        hovertemplate="<b>%{y}</b><br>%{x:,.0f} €"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="league_market_values"

    )


def display_average_age_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="average_age",

        y="club",

        orientation="h",

        text="average_age",

        color="average_age",

        color_continuous_scale="Oranges"

    )

    figure.update_layout(

        title="Average Squad Age",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=700

    )

    figure.update_traces(

        texttemplate="%{text:.1f} years",

        hovertemplate="<b>%{y}</b><br>%{x:.1f} years"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="league_average_age"

    )


def display_top_scorers_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="goals",

        y="player",

        orientation="h",

        color="goals",

        text="goals",

        hover_data=["club"],

        color_continuous_scale="Reds"

    )

    figure.update_layout(

        title="Top Scorers",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=600

    )

    figure.update_traces(

        texttemplate="%{text}",

        hovertemplate="<b>%{y}</b><br>%{customdata[0]}<br>%{x} goals"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="league_top_scorers"

    )

def display_top_assists_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="assists",

        y="player",

        orientation="h",

        color="assists",

        text="assists",

        hover_data=["club"],

        color_continuous_scale="Greens"

    )

    figure.update_layout(

        title="Top Assists",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=600

    )

    figure.update_traces(

        texttemplate="%{text}",

        hovertemplate="<b>%{y}</b><br>%{customdata[0]}<br>%{x} assists"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="league_top_assists"

    )

def display_most_offensive_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="goals",

        y="club",

        orientation="h",

        color="goals",

        text="goals",

        color_continuous_scale="Sunset"

    )

    figure.update_layout(

        title="Most Offensive Clubs",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=650

    )

    figure.update_traces(

        texttemplate="%{text}",

        hovertemplate="<b>%{y}</b><br>%{x} goals"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="league_offensive"

    )


def display_most_creative_chart(data):

    dataframe = pd.DataFrame(data)

    figure = px.bar(

        dataframe,

        x="assists",

        y="club",

        orientation="h",

        text="assists",

        color="assists",

        color_continuous_scale="Greens"

    )

    figure.update_layout(

        title="Most Creative Clubs",

        yaxis=dict(

            categoryorder="total ascending"

        ),

        coloraxis_showscale=False,

        height=650

    )

    figure.update_traces(

        texttemplate="%{text}",

        hovertemplate="<b>%{y}</b><br>%{x} assists"

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="creative"

    )

def display_attack_scatter(data):

    dataframe = pd.DataFrame(data)

    figure = px.scatter(

        dataframe,

        x="goals",

        y="assists",

        text="club",

        size="goals",

        color="goals",

        color_continuous_scale="Turbo"

    )

    figure.update_traces(

        textposition="top center",

        marker=dict(

            line=dict(

                width=1,

                color="white"

            )

        )

    )

    figure.update_layout(

        title="Goals vs Assists",

        xaxis_title="Goals",

        yaxis_title="Assists",

        coloraxis_showscale=False,

        height=700

    )

    st.plotly_chart(

        figure,

        use_container_width=True,

        key="attack_scatter"

    )