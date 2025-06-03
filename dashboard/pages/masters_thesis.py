import streamlit as st
import altair as alt
import streamlit.components.v1 as components

# This must be the first Streamlit command
st.set_page_config(
    page_title="The Escape from Gaza",
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
st.title("Seeking Truth in A Time of War")
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
st.write("In Jehad al-Saftawi's final year of trying to flee Gaza for a new life in the United States, sheer desperation consumed him. He even fleetingly entertained the impulsive idea of running to the Israel border. As a photographer and journalist, he no longer wanted to exist in a place without a free press and where danger and suspicions were ever-present. ")
st.text("")
st.write("Al-Saftawi is the son of a jihadist who belonged to one of the leading armed factions in Gaza, but he viewed the world through a far different lens than his father. He condemned the killing of innocent people on both sides of a centuries-old conflict and longed to leave behind the pain and hopelessness he felt.")
st.text("")
st.write("How can humans organize themselves this vastly apart from one another? he wondered.")
st.text("")
st.write("After three rejections from Israeli security, al-Saftawi was allowed to cross the border in 2016 for an interview at the U.S. Consulate connected to his asylum application. He had heard stories of Palestinians who dared to cross into Israel only to be captured by the army, but he was willing to take almost any risk.")
st.text("")
st.write("The nearly two-hour taxi ride to the Consulate provided time to reflect on his childhood in Gaza and Syria, and the aspirations he had as a boy. A strange yet familiar feeling also came over the 25-year-old. The last time he stepped foot in Jerusalem, he was 14 and there to visit his father in a prison. Al-Saftawi looked out at the homes that dotted the landscape, noting with a critical eye their prosperity compared to neighborhoods he knew in Gaza.")
st.text("")
st.write("As the taxi drove up to the Consulate’s roundabout, a group of his Israeli friends waited outside, embracing him.")
st.text("")
st.write("Al-Saftawi caught his breath before stepping inside to join a queue. The person in front of him was an Israeli citizen, also trying to emigrate to the United States. He reflected on their differences and, at this moment, their similarities.")
st.text("")
st.write("“Do you want to go to Al-Aqsa Mosque?” his friend Athir inquired after the interview.")
st.text("")
st.write("“No, I don’t want to do anything with this contentious place,” al-Saftawi replied.")
st.text("")
st.write("They rested under trees in the periphery of the consulate. Al-Saftawi felt as though everyone was looking at him like an outsider, feeling sad for him. But if they looked closer, they could see the hope in his eyes. Leaving Gaza was more tangible now than ever.")
st.text("")
st.write("“I don’t want to go back,” he said, crying.")
st.text("")
st.write("Later that afternoon, Athir drove him to the Gaza border, where al-Saftawi crossed into his homeland and waited anxiously for another two months to receive approval from the Consulate. When word came, he and his wife, Lara Aburamadan, had just 72 hours to leave Gaza, beginning a dangerous journey that took them through Egypt for a flight to New York. Eventually, they moved to the San Francisco Bay Area, where they continued to go through the asylum process – and where, in 2023, the long tail of the Israel-Palestine conflict disrupted their lives as visual storytellers.")

# Enable Altair dark theme
alt.themes.enable("dark")