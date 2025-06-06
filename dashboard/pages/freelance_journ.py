import streamlit as st
import altair as alt
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd
import os

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
st.title("The Dangers Freelance Journalists Face")
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
st.write("Freelance journalists are independent journalists that work on a freelance basis, often covering stories in conflict zones or areas of political unrest. They face unique challenges and dangers, including lack of institutional support, financial instability, and exposure to violence. ")
st.text("")
st.write("There were 236 freelance journalists killed and 101 of those were murdered with intent. About 40% of the killed freelance journalists were murdered intentionally. The number of freelance journalists killed was 47 journalists since Oct. 7, 2023. This page explores the risks they encounter and the impact of their work on journalism and society.")
st.text("")
st.write("Since 1992, there were 58 freelance journalists killed due to crossfire, 74 on a dangerous assignment and three had unknown deaths. Freelance journalists are killed more than any other journalist since they normally contract themselves, which allows for greater risks since they are not tied to a news organization.")

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
        # Create a selection tool for year
        year_selection = alt.selection_single(
            fields=['Year'],
            bind=alt.binding_select(options=sorted(cpj['Year'].dropna().unique())),
            name="Select Year"
        )



freelance_type_of_death = cpj[cpj['organizations'].isin(['Freelance', 'Freelancer'])].groupby('typeOfDeath').size().reset_index(name='Count')

# Create scatter plot with updated style
scatter_plot_freelance = alt.Chart(freelance_type_of_death).mark_circle().encode(
    x=alt.X('Count:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('typeOfDeath:N', title='Type of Death', axis=alt.Axis(titleColor='white', labelColor='white')),
    size=alt.Size('Count:Q', scale=alt.Scale(range=[100, 1000]), legend=None),
    color=alt.Color('typeOfDeath:N', scale=alt.Scale(scheme='tableau10'), legend=alt.Legend(title="Type of Death", titleColor='white', labelColor='white')),
    tooltip=[]
).properties(
    title=alt.TitleParams(
        text='Freelance Journalists Increasingly Murdered Since 1992',
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

# Show scatter plot in streamlit
st.altair_chart(scatter_plot_freelance, use_container_width=True)

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st.write("The top news organization with the highest number of journalist deaths include freelancers with 236 deaths, Reuters with 14 deaths, Al-Aqsa TV with 11 deaths, Al-Jazeera with ten deaths, Algerian State Television with 9 deaths, Al-Iraqiya with 8 deaths, Baghdad TV with 8 deaths, Al-Arabiya with 7 deaths, Radio Shabelle with six deaths and Ozgur Gundem with six deaths.")

# Count the number of deaths for each type of death for freelance journalists
news_orgs_deaths = cpj.groupby('organizations').size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)
# Merge "Freelance" and "Freelancer" into a single category "Freelance"
news_orgs_deaths['organizations'] = news_orgs_deaths['organizations'].replace(['Freelancer'], 'Freelance')

# Recalculate the counts after merging
news_orgs_deaths = news_orgs_deaths.groupby('organizations', as_index=False).sum().sort_values(by='Deaths', ascending=False)
# Create a bar chart for the top 10 news organizations with the highest number of journalist deaths
top_10_news_orgs_chart = alt.Chart(news_orgs_deaths.head(10)).mark_bar().encode(
    x=alt.X('Deaths:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('organizations:N', title='News Organization', sort='-x', axis=alt.Axis(titleColor='white', labelColor='white')),
    color=alt.Color('Deaths:Q', scale=alt.Scale(scheme='blues'), legend=None),  # Light-to-dark blue shades
    tooltip=[]  # Add hover tooltip
).properties(
    title=alt.TitleParams(
        text='Top 10 News Organizations with the Highest Number of Journalist Deaths since 1992',
        subtitle="The bars represent the number of journalist deaths for each organization.",
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

# Display the bar chart in streamlit
st.altair_chart(top_10_news_orgs_chart, use_container_width=True)

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

st. write("The top locations with the highest number of freelance deaths include Israel and the Occupied Palestinian Territory with 50 deaths, Syria with 39 deaths, Iraq with 21 deaths, Mexico with ten deaths, and Somalia with nine deaths. Ukraine, Bangladesh, Bosnia, Pakistan and Libya each had six freelancer deaths at these locations.")

# Track locations with the highest number of journalist deaths for freelancers
freelance_locations = cpj[cpj['organizations'].isin(['Freelance', 'Freelancer'])].groupby('location').size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)
# Display the top 10 locations with the highest number of journalist deaths for freelancers
print("Top 10 locations with the highest number of journalist deaths for freelancers:")
print(freelance_locations.head(10))
# Create a bar chart for the top 10 locations with the highest number of journalist deaths for freelancers
freelance_locations_chart = alt.Chart(freelance_locations.head(10)).mark_bar().encode(
    x=alt.X('Deaths:Q', title='Number of Deaths', axis=alt.Axis(titleColor='white', labelColor='white')),
    y=alt.Y('location:N', title='Location', sort='-x', axis=alt.Axis(titleColor='white', labelColor='white')),
    color=alt.Color('Deaths:Q', scale=alt.Scale(scheme='blues'), legend=None),  # Light-to-dark blue shades
    tooltip=[]  # Add hover tooltip
).properties(
    title=alt.TitleParams(
        text='Top 10 Locations with the Highest Number of Journalist Deaths for Freelancers since 1992',
        subtitle="The bars represent the number of journalist deaths for each location.",
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

# Display the bar chart in streamlit
st.altair_chart(freelance_locations_chart, use_container_width=True)

# Add data source and byline
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p><em>Source: <a href="https://cpj.org/data/" target="_blank" style="color: #FAFAFA;">Committee to Protect Journalists</a> / Credits: Michaela Herbst</em></p>
    </div>
""", unsafe_allow_html=True)

# Enable Altair dark theme
alt.themes.enable("dark")