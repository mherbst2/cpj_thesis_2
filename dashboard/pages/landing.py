import streamlit as st
import altair as alt
import pandas as pd
import csv
import streamlit.components.v1 as components
from vega_datasets import data
import os
from pathlib import Path



# This must be the first Streamlit command
st.set_page_config(
    page_title="Seeking Truth in A Time of War",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .block-container { padding-top: 0rem; }
    .stApp { background-color: #000; }
    h1, h2, h3, h4, h5, h6, p, div, span { color: #FAFAFA !important; }
    .css-6qob1r { background-color: #111 !important; }
    header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("Silencing Stories: The Legacy of Journalists")
st.write("Since 1992, the Committee to Protect Journalists has documented the killings of 1,687 journalists around the world. My master's thesis, 'Seeking Truth in A Time of War,' tells the story of Jehad al-Saftawi, a Gaza photojournalist. Al-Saftawi's story shows how even though he escaped the bloodshed of Gaza, his past still haunts him in the United States. The dashboard is a tribute to all journalists who have lost their lives in the pursuit of truth and justice.")


st.markdown(
    """
    <style>
        /* Sidebar background to black */
        section[data-testid="stSidebar"] {
            background-color: black;
        }

        /* Sidebar text color to black */
        section[data-testid="stSidebar"] * {
            color: black;
        }

        /* Main content background to white */
        .main {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
current_directory = Path(os.getcwd()).resolve()
DATA_DIR = current_directory.parent.joinpath('data')
DATA_DIR.mkdir(parents=True, exist_ok=True)
cpj = pd.read_csv("data/cpj.csv")
# Ensure the CSV file is loaded correctly
if cpj.empty:
    st.error("The DataFrame is empty. Please check the CSV file.")
else:
    # Ensure 'Year' and 'Month' columns exist
    if 'Date' in cpj.columns:
        cpj['Year'] = pd.to_datetime(cpj['Date']).dt.year
        cpj['Month'] = pd.to_datetime(cpj['Date']).dt.month_name()
    else:
        st.error("The 'Date' column is missing in the CSV file. Please check the data source.")

    # Create a selection tool for the year using selection_point
    year_selection = alt.selection_point(
        fields=['Year'],
        bind=alt.binding_select(options=list(range(1992, 2026)), name='Select Year'),
        name='Year'
    )

    # Filter data based on the selected year
    month_deaths_chart = alt.Chart(cpj).mark_bar().encode(
        x=alt.X('Month:O', title='Month', sort=[
            'January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December'
        ], axis=alt.Axis(labelAngle=45)),  # Rotate month labels by 45 degrees
        y=alt.Y('count():Q', title='Number of Deaths'),
        color=alt.Color('Month:O', legend=None),
        tooltip=['Month:O', 'count():Q']
    ).add_params(
        year_selection
    ).transform_filter(
        year_selection
    ).properties(
        title='Journalists Killed per Month (Filtered by Year)',
        width=800,
        height=400,
        background='#111',  # Set chart background to dark
        padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
    )
    # Display the chart
    st.altair_chart(month_deaths_chart, use_container_width=True)

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

