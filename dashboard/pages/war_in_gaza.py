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
st.write("On Oct. 7, 2023, Hamas, a nationalist political organization launched an attack killing about 1,200 people, most of them civilians, and led to more than 250 hostages being taken. Israel's counterattack resulted in the killing of more than 48,000 Palestinians according to Reuters. On Nov. 21, 2023 Israel and Hamas declared a truce including the release of about half of the hostages.")
st.text("")
st.write("However, the war continued ten days later. The month with the largest number of deaths between late 2023 and May 2025 was October with 28 deaths. In October 2023, 27 journalists were killed on a dangerous assignment and one was murdered. There were 26 journalists killed on a dangerous assignment in the Israel and Occupied Palestinian territory, one journalist was murdered with intent in Lebanon and was killed on a dangerous assignment in Sudan.")

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
    color=alt.Color('Year:N', legend=alt.Legend(title="Year", titleColor='white', labelColor='white')),
    tooltip=[]  # Add tooltip with Year, Month, and Deaths
).properties(
    title=alt.TitleParams(
        text='Journalists Killed at Increasing Rate since October 2023 - May 2025',
        subtitle="The bars represent the number of journalists killed each month, with the colors indicating the years.",
        color='white',  # Set title color to white
        subtitleColor='white'  # Set subtitle color to white
    ),
    width=800,
    height=400,
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).configure_axis(
    grid=True,  # Enable gridlines
    gridColor='white',  # Set gridline color
    gridOpacity=0.3  # Set gridline opacity
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

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st.write("The category that accounted for the highest number of journalist deaths over 2023-2025 was due to dangerous assignments. Since 2023, there were 163 journalists killed due to dangerous assignments, 4 due to crossfire and 33 were murdered with intent. There were 147 journalists that were killed on a dangerous assignment and 12 that were murdered with intent in the Israel and Palestine Occupied Territory.")
# Add chart for type of deaths
# Filter data for the date range from October 7, 2023, to the present
filtered_date_range = cpj[cpj['Date'] >= '2023-10-07']

# Group by 'typeOfDeath' and count occurrences for the filtered date range
type_of_death_counts_filtered = filtered_date_range.groupby('typeOfDeath').size().reset_index(name='Count')
# Create scatter plot with consistent style
scatter_plot = alt.Chart(type_of_death_counts_filtered).mark_circle().encode(
    x=alt.X('Count:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('typeOfDeath:N', title='Type of Death', axis=alt.Axis(titleColor='white', labelColor='white')),
    size=alt.Size('Count:Q', scale=alt.Scale(range=[100, 1000]), legend=None),
    color=alt.Color('typeOfDeath:N', scale=alt.Scale(scheme='tableau10'), legend=alt.Legend(title="Type of Death", titleColor='white', labelColor='white')),
    tooltip=[alt.Tooltip(), alt.Tooltip()]
).properties(
    title=alt.TitleParams(
        text='Journalists Increasingly Killed By Dangerous Assignments since 2023',
        subtitle="Bubble size represents the number of deaths for each type of death.",
        color='white',  # Set title color to white
        subtitleColor='white'  # Set subtitle color to white
    ),
    width=800,
    height=400,
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).configure_axis(
    grid=True,  # Enable gridlines
    gridColor='white',  # Set gridline color
    gridOpacity=0.3  # Set gridline opacity
).configure_view(
    stroke=None
).configure_title(
    fontSize=16,
    fontWeight='bold',
    anchor='start',
    color='white'
)

# Display chart in Streamlit
st.altair_chart(scatter_plot, use_container_width=True)
# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st.write("In October 2023, 35 journalists were killed on a dangerous assignment. There were 27 journalists killed in November during a dangerous assignment. In December, 23 journalists were killed on a dangerous assignment while four were murdered with intent.")

# Create a bar chart showing deaths in Israel and the Occupied Palestinian Territory per month and type of death
israel_palestine_deaths = filtered_months[filtered_months['location'] == "Israel and the Occupied Palestinian Territory"]
israel_palestine_deaths = filtered_months[filtered_months['location'] == "Israel and the Occupied Palestinian Territory"]

# Update the year selection to only include 2023-2025
year_selection = alt.selection_point(
    fields=['Year'],
    bind=alt.binding_select(options=[2023, 2024, 2025], name='Select Year'),
    name='Year'
)
# Create a bar chart showing deaths in Israel and the Occupied Palestinian Territory per month and type of death, filtered by year
chart = alt.Chart(israel_palestine_deaths).mark_bar().encode(
    x=alt.X('Month:O', title='Month', sort=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ], axis=alt.Axis(labelAngle=45, titleColor='white', labelColor='white')),
    y=alt.Y('count():Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    color=alt.Color('typeOfDeath:N', title='Type of Death', scale=alt.Scale(scheme='tableau10'), legend=alt.Legend(titleColor='white', labelColor='white')),
    tooltip=[]
).add_params(
    year_selection
).transform_filter(
    year_selection
).properties(
    title=alt.TitleParams(
        text='Journalist Deaths in Israel and the Occupied Palestinian Territory by Month and Type of Death',
        subtitle="The bars represent the number of deaths each month, categorized by type of death.",
        color='white',  # Set title color to white
        subtitleColor='white'  # Set subtitle color to white
    ),
    width=800,
    height=400,
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).configure_axis(
    grid=True,  # Enable gridlines
    gridColor='white',  # Set gridline color
    gridOpacity=0.3  # Set gridline opacity
).configure_view(
    stroke=None
).configure_title(
    fontSize=16,
    fontWeight='bold',
    anchor='start',
    color='white'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)