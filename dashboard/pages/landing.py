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
st.subheader("By Michaela Herbst")
st.write("Journalism is an essential part of our democracy as it keeps those in power  accountable, informs citizens and acts as the unofficial fourth branch of government. The dashboard is a tribute to all journalists who have lost their lives in the pursuit of truth and justice. The state of journalism is at risk due to increased threats by government officials and safety issues. Political leaders have called the press the enemy of the people. The Trump Administration has decided to choose which media organizations can be allowed in the White House press briefing room. By blocking media outlets that have been allowed in the White House for decades, he is further perpetuating the idea of confirmation bias.")
st.text("")
st.write("In order to do this profession ethically, journalists follow the core ten elements of journalism. Bill Kovach and Tom Rosenstiel are influential journalists who outlined these principles in their book, “The Elements of Journalism.” These include: (1) journalism's first obligation is to the truth, (2) loyalty to citizens, (3) verification, (4) maintaining independence, (5) monitors power, (6) provides a public forum, (7) has a purpose, (8) comprehensive, (9) exercise in personal conscience, and (10) holds responsibility. According to the United Nations, journalism continues to remain a deadly profession, “and nine times out of ten, the murder of a journalist is unresolved.” Journalists continue to seek truth in the midst of utter chaos that occurs around them.")
st.text("")
st.write("“Stop targeting truth and truth-tellers,” said Antonio Guterres, the United Nations Secretary-General. “As journalists stand up for truth, the world stands with them.”")
st.text("")
st.write("Since 1992, the Committee to Protect Journalists (CPJ) has documented the killings of 1,687 journalists around the world. The CPJ is an independent organization that helps protect the rights of journalists by promoting the freedom of the press. They track whether journalists were murdered, died during crossfire or on a dangerous assignment. On average, about 140 journalists are killed globally per month.")


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
        tooltip=[]  # Add tooltip for month and count
        ).add_params(
        year_selection
        ).transform_filter(
        year_selection
        ).properties(
        title=alt.TitleParams(
            text='Journalists Killed Globally per Month from 1992-2025',
            subtitle="The bars represent the number of journalists killed each month from 1992 to 2025. The data is filtered by the selected year.",
            color='white',  # Set title color to white
            subtitleColor='white'  # Set subtitle color to white
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

st.write("There were 992 journalists murdered with intent since 1992, accounting for nearly 60% of all journalist deaths. There were 355 journalists killed due to a dangerous assignment. There were 328 journalists killed due to combat or crossfire and 12 journalists were killed by an unknown source.")

# Filter'typeOfDeath' column for 'Murder'
murder_deaths = cpj[cpj['typeOfDeath'] == 'Murder']

# Count the number of murder_deaths
murder_deaths.count()

# Create type_of_death_counts
# Group by 'typeOfDeath' and count occurrences
type_of_death_counts = cpj.groupby('typeOfDeath').size().reset_index(name='Count')

# Rename the column for clarity
type_of_death_counts = type_of_death_counts.rename(columns={'typeOfDeath': 'Type of Death'})

# Merge 'Crossfire' and 'Crossfire / Combat Related' into one category
type_of_death_counts['Type of Death'] = type_of_death_counts['Type of Death'].replace(
    ['Crossfire', 'Crossfire / Combat Related'], 'Crossfire/Combat Related'
)
# Recalculate the counts after merging
type_of_death_counts = type_of_death_counts.groupby('Type of Death', as_index=False).sum()
type_of_death_counts_chart = alt.Chart(type_of_death_counts).mark_circle(
    opacity=0.8,
    stroke='white',
    strokeWidth=1,
    strokeOpacity=0.4
).encode(
    alt.Y('Type of Death:N')
        .title('Type of Death')
        .axis(labelColor='white', titleColor='white'),  # Set Y-axis text color to white
    alt.X('Count:Q')
        .title('Number of Deaths')
        .axis(labelColor='white', titleColor='white'),  # Set X-axis text color to white
    alt.Size('Type of Death:N', scale=alt.Scale(domain=['Dangerous Assignment', 'Murder', 'Crossfire/Combat Related'], range=[800, 400, 400]), legend=None)
        .title('Deaths'),
    alt.Color('Type of Death:N').legend(None),
    tooltip=[],  # Add tooltip for type of death and count
).properties(
    width=800,
    height=400,
    title=alt.Title(
        text="The Types of Deaths Journalists Endured from 1992-2025",
        subtitle="The size of the bubble represents the total death count for each type of death.",
        anchor='start',
        subtitleColor='white'  # Set subtitle color to white
    ),
    background='#111',  # Set chart background to dark
    padding={"top": 10, "bottom": 10, "left": 10, "right": 10}
).configure_axisY(
    domain=False,
    ticks=False,
    offset=10
).configure_axisX(
    domain=False,
    ticks=False,
    offset=10
).configure_view(
    stroke=None
).configure_title(
    fontSize=16,
    fontWeight='bold',
    anchor='start',
    color='white'
).configure_legend(
    labelFontSize=12,
    titleFontSize=14
)

# Display the chart
st.altair_chart(type_of_death_counts_chart, use_container_width=True)
# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st.write("The top locations with the highest number of journalist deaths include: Iraq, Israel and the Occupied Palestinian Territory, Syria, Philippines, Somalia, Pakistan, Mexico, India, Russia and Algeria. On a global level, the location that experienced the highest number of journalist deaths was Iraq with 193 deaths. The second was Israel and the Occupied Palestinian Territory with 178 deaths.")

# Add a bar chart with the top 10 locations with the most journalist deaths
global_deaths = cpj.groupby('location').size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)
top_10_locations = global_deaths.head(10)
top_10_locations_chart = alt.Chart(global_deaths).mark_bar().encode(
    x=alt.X('Deaths:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('location:N', title='Location', sort='-x', axis=alt.Axis(titleColor='white', labelColor='white')),  # Sort by number of deaths
    color=alt.Color('Deaths:Q', scale=alt.Scale(scheme='blues'), legend=None),  # Light-to-dark blue shades
    tooltip=[]  # Add hover tooltip for location and number of deaths
).transform_window(
    rank='rank(Deaths)',
    sort=[alt.SortField('Deaths', order='descending')]
).transform_filter(
    alt.datum.rank <= 10  # Filter top 10 locations
).properties(
    title=alt.TitleParams(
        text='Top 10 Locations with the Highest Number of Journalist Deaths since 1992',
        subtitle="The bars represent the number of journalists killed in each location from 1992 to 2025. The data is filtered to show only the top 10 locations with the highest number of deaths.",
        color='white',  # Set title color to white
        subtitleColor='white'  # Set subtitle color to white
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

st.write("On Oct. 7, 2023, Hamas a nationalist political organization, launched an attack on Israel, continuing the ongoing Israeli-Palestinian conflict. My master's thesis, 'Seeking Truth in A Time of War,' tells the story of Jehad al-Saftawi, a Gaza photojournalist. Al-Saftawi's story shows how even though he escaped the bloodshed of Gaza, his past still haunts him in the United States.")


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

