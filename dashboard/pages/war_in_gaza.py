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
st.title("The War in Gaza and the Press")
st.markdown(
    """
    <style>
        /* Sidebar background to black */
        section[data-testid="stSidebar"] {
            background-color: black;
        }

        /* Sidebar text color to white */
        section[data-testid="stSidebar"] * {
            color: white;
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
st.write("On Oct. 7, 2023, Hamas, a nationalist political organization launched an attack killing about 1,200 people, most of them civilians, and led to more than 250 hostages being taken. The Israel-Palestine conflict dates back to t")

# Enable Altair dark theme
alt.themes.enable("dark")

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
# Filter data for deaths between Oct. 7, 2023, and May 31, 2025
filtered_months = cpj[(cpj['Date'] >= '2023-10-07') & (cpj['Date'] <= '2025-05-31')]

# Group by Year and Month and count the number of deaths
deaths_by_month = filtered_months.groupby(['Year', 'Month']).size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)

# What is the month with the largest number of deaths?
largest_death_month = deaths_by_month.iloc[0]
print(f"The month with the largest number of deaths is {largest_death_month['Month']} {largest_death_month['Year']} with {largest_death_month['Deaths']} deaths.")

# Create a bar chart for the number of deaths by month with a dark theme
bar_chart = alt.Chart(deaths_by_month).mark_bar().encode(
    x=alt.X('Month:O', title='Month', sort=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ], axis=alt.Axis(labelAngle=45, titleColor='white', labelColor='white')),  # Rotate x-axis labels by 45 degrees
    y=alt.Y('Deaths:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    color=alt.Color('Year:N', legend=None),
    tooltip=[]
).properties(
    title=alt.TitleParams(
        text='Journalists Killed at Increasing Rate since October 2023 - May 2025',
        color='white',  # Set title color to white
    ),
    width=800,
    height=400,
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).configure_axis(
    grid=False
).configure_view(
    stroke=None
).configure_title(
    fontSize=16,
    fontWeight='bold',
    anchor='start',
    color='white'
)

# Display the bar chart
st.altair_chart(bar_chart, use_container_width=True)
