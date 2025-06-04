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
st.write("Journalism is an essential part of our demcoracy as it keeps those in power  accountable, informs citizens and acts as the unofficial fourth branch of government. The state of journalism is However, political leaders have called the press the enemy of the people. The Trump Administration has decided to choose which media organizations can be allowed in the White House press briefing room. By blocking media outlets that have been allowed in the White House for decades, he is further perpetuating the idea of confirmation bias.")
st.text("")
st.write("According to the United Nations, journalism continues to remain a deadly profession, “and nine times out of ten, the murder of a journalist is unresolved.”")
st.text("")
st.write("“Stop targeting truth and truth-tellers,” said Antonio Guterres, the United Nations Secretary-General. “As journalists stand up for truth, the world stands with them.”")
st.text("")
st.write("Since 1992, the Committee to Protect Journalists has documented the killings of 1,687 journalists around the world. The Committee to Protect Journalists is an independent organization helps protect the rights of journalists by promoting the freedom of the press. The Committee to Protect Journalists tracks whether journalists were murdered, died during crossfire or on a dangerous assignment.")

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
        ], axis=alt.Axis(labelAngle=45, titleColor='white', labelColor='white')),  # Rotate month labels by 45 degrees
        y=alt.Y('count():Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
        color=alt.Color('Month:O', legend=None),
        tooltip=[]
        ).add_params(
        year_selection
        ).transform_filter(
        year_selection
        ).properties(
        title=alt.TitleParams(
            text='Journalists Killed Globally per Month',
            color='white'  # Set title color to white
        ),
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

# Add a bar chart with the top 10 locations with the most journalist deaths
global_deaths = cpj.groupby('location').size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)
top_10_locations = global_deaths.head(10)

top_10_locations_chart = alt.Chart(global_deaths).mark_bar().encode(
    x=alt.X('Deaths:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('location:N', title='Location', sort='-x', axis=alt.Axis(titleColor='white', labelColor='white')),  # Sort by number of deaths
    color=alt.Color('Deaths:Q', scale=alt.Scale(scheme='blues'), legend=None),  # Light-to-dark blue shades
    tooltip=[]  # Add hover tooltip
).transform_window(
    rank='rank(Deaths)',
    sort=[alt.SortField('Deaths', order='descending')]
).transform_filter(
    alt.datum.rank <= 10  # Filter top 10 locations
).properties(
    title=alt.TitleParams(
        text='Top 10 Locations with the Highest Number of Journalist Deaths since 1992',
        color='white'  # Set title color to white
    ),
    width=800,
    height=400,
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).interactive()  # Enable hover interaction
# Display the bar chart
st.altair_chart(top_10_locations_chart, use_container_width=True)
# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st.write("On Oct. 7, 2023, Hamas a nationalist political organization launched an attack on Israel, continuing the ongoing Israeli-Palestinian conflict. My master's thesis, 'Seeking Truth in A Time of War,' tells the story of Jehad al-Saftawi, a Gaza photojournalist. Al-Saftawi's story shows how even though he escaped the bloodshed of Gaza, his past still haunts him in the United States. The dashboard is a tribute to all journalists who have lost their lives in the pursuit of truth and justice.")


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

