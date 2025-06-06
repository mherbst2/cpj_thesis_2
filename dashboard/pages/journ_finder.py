import streamlit as st
import altair as alt
import pandas as pd
import csv
import streamlit.components.v1 as components
from vega_datasets import data
import os
from pathlib import Path
# --- Page Config ---
st.set_page_config(
    page_title="Seeking Truth in A Time of War",
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
<style>
.block-container { padding-top: 0rem; }
.stApp { background-color: #111; color: #FAFAFA; }
section[data-testid="stSidebar"] {
    background-color: #000;
}
section[data-testid="stSidebar"] * {
    color: #FFF;
}
header { visibility: hidden; }
.card {
    background-color: #222;
    color: #FAFAFA;
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.card h4 { margin-top: 0.5rem; margin-bottom: 0.2rem; }
.card p { margin: 0.2rem 0; }
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Journalist Finder")

# --- Load Data ---
current_directory = Path(os.getcwd()).resolve()
DATA_DIR = current_directory.parent.joinpath('data')
PHOTO_DIR = DATA_DIR / "card_photos"
cpj = pd.read_csv("data/cpj.csv")
journalists_killed_october_2023_csv = DATA_DIR / "journalists_killed_october_2023.csv"

# Filter data for deaths between Oct. 7, 2023, and May 31, 2025
filtered_months = cpj[(cpj['Date'] >= '2023-10-07') & (cpj['Date'] <= '2025-05-31')]

# Group by Year and Month and count the number of deaths
deaths_by_month = filtered_months.groupby(['Year', 'Month']).size().reset_index(name='Deaths').sort_values(by='Deaths', ascending=False)

# Filter for journalists killed in Israel and the Occupied Palestinian Territory from Oct. 7, 2023, to Oct. 31, 2023
journalists_killed_october_2023 = filtered_months[
    (filtered_months['location'] == "Israel and the Occupied Palestinian Territory") &
    (filtered_months['Date'] >= '2023-10-07') &
    (filtered_months['Date'] <= '2023-10-31')
]

# Display the filtered DataFrame
print(journalists_killed_october_2023)

#save to csv file of journalists_killed_october_2023
journalists_killed_october_2023_csv = DATA_DIR / "journalists_killed_october_2023.csv"
# Save the filtered DataFrame to a new CSV file
journalists_killed_october_2023.to_csv(journalists_killed_october_2023_csv, index=False)
# --- Preprocess ---
if journalists_killed_october_2023.empty:
    st.error("The DataFrame is empty. Please check the CSV file.")
else:
    if 'Date' in journalists_killed_october_2023.columns:
        # Ensure 'Date' is in datetime format
        journalists_killed_october_2023['Date'] = pd.to_datetime(journalists_killed_october_2023['Date'], errors='coerce')
        if journalists_killed_october_2023['Date'].isnull().all():
            st.error("The 'Date' column could not be converted to datetime. Please check the CSV file.")
        else:
            journalists_killed_october_2023['Year'] = journalists_killed_october_2023['Date'].dt.year
    else:
        st.error("The 'Date' column is missing in the CSV file.")

# --- Search Input ---
text_search = st.text_input(
    "Search for a journalist by name", 
    value="", 
    key="text_search", 
    label_visibility="visible"
)

# Add CSS to make the input text white
st.markdown("""
<style>
div[data-testid="stTextInput"] > div > input {
    color: #FFF !important;
    background-color: #000 !important; /* Ensure the background is black */
}
</style>
""", unsafe_allow_html=True)

if text_search:
    search_results = journalists_killed_october_2023[journalists_killed_october_2023['fullName'].str.contains(text_search, case=False, na=False)]
    if not search_results.empty:
        st.write(f"Found {len(search_results)} result(s):")
        for _, row in search_results.iterrows():
            st.write(f"- {row['fullName']}")
    else:
        st.write("No results found.")
else:
    st.write("This search tool shows journalists who were killed right after the Oct. 7, 2023 Hamas attacks.")

# --- Filter Data ---
if text_search:
    filtered = journalists_killed_october_2023[journalists_killed_october_2023['fullName'].str.contains(text_search, case=False, na=False)]
else:
    filtered = journalists_killed_october_2023.copy()

# --- Helper Function ---
def name_to_filename(name):
    return name.lower().replace(" ", "_").replace(".", "").replace(",", "") + ".jpg"

# Display Abdulhadi Habib's card
photo_path_habib = current_directory / "data" / "card" / "photos" / "abdulhadi_habib.jpg"
if photo_path_habib.exists():
    st.image(photo_path_habib, caption="Abdulhadi Habib", width=200)
    st.markdown("""
    <div class="card">
        <h4>Abdulhadi Habib</h4>
        <p>Abdulhadi Habib, 37, worked as an internet reporter at Al-Manara News Agency. He was killed in Northern Gaza and covered culture, human rights and war. Habib died on Oct. 16, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_habib}")

# Display Ahmed Abu Mhadi's card
photo_path_mhadi = current_directory / "data" / "card" / "photos" / "ahmed_abu_mhadi.jpg"
if photo_path_mhadi.exists():
    st.image(photo_path_mhadi, caption="Ahmed Abu Mhadi", width=200)
    st.markdown("""
    <div class="card">
        <h4>Ahmed Abu Mhadi</h4>
        <p>Ahmed Abu Mhadi, 29, was a photojournalist for Al-Quds News Network. He was killed in Southern Gaza while documenting the aftermath of airstrikes. Mhadi died on Oct. 18, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_mhadi}")


# Display Ahmed Shehab's card
photo_path_shehab = current_directory / "data" / "card" / "photos" / "ahmed_shehab.jpg"
if photo_path_shehab.exists():
    st.image(photo_path_shehab, caption="Ahmed Shehab", width=200)
    st.markdown("""
    <div class="card">
        <h4>Ahmed Shehab</h4>
        <p>Ahmed Shehab was a broadcast radio reporter for Sowt Al-Asra Radio. He was killed with his three children and wife during an Israeli airstrike. He died on Oct. 12, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_shehab}")

# Display Duaa Sharaf's card
photo_path_shehab = current_directory / "data" / "card" / "photos" / "duaa_sharaf.jpg"
if photo_path_shehab.exists():
    st.image(photo_path_shehab, caption="Duaa Sharaf", width=200)
    st.markdown("""
    <div class="card">
        <h4>Duaa Sharaf</h4>
        <p>Duaa Sharaf was a  Radio Al-Aqsa journalist who was killed in an airstrike with her child. She died on Oct. 16, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_shehab}")


# Display Hisham Alnwajha card
photo_path_shehab = current_directory / "data" / "card" / "photos" / "hisham_alnwajha.jpg"
if photo_path_shehab.exists():
    st.image(photo_path_shehab, caption="Hisham Alnwajha", width=200)
    st.markdown("""
    <div class="card">
        <h4>Hisham Alnwajha</h4>
        <p>Hisham Alnwajha, 27, was a reporter for the Khabar News Agency. He was killed in the midst of a dangerous assignment as warplanes struck. He was killed on Oct. 9, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_shehab}")

# Display Husam Mubarak's card
photo_path_shehab = current_directory / "data" / "card" / "photos" / "husam_mubarak.jpg"
if photo_path_shehab.exists():
    st.image(photo_path_shehab, caption="Husam Mubarak", width=200)
    st.markdown("""
    <div class="card">
        <h4>Husam Mubarak</h4>
        <p>Husam Mubarak was a journalist at Al Aqsa Radio and was killed in an Israeli airstrike while he was on a dangerous assignment. He was killed on Oct. 13, 2023. </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_shehab}")

# Display Ibrahim Mohammad Lafi's card 
photo_path_ibrahim = current_directory / "data" / "card" / "photos" / "ibrahim_mohammad_lafi.jpg"
if photo_path_ibrahim.exists():
    st.image(photo_path_ibrahim, caption="Ibrahim Mohammad Lafi", width=200)
    st.markdown("""
    <div class="card">
        <h4>Ibrahim Mohammad Lafi</h4>
        <p>Ibrahim Mohammad Lafi was a photojournalist for Ain Media who covered culture and war. He was killed on Oct. 7, 2023 on the Gaza Strip.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_ibrahim}")

# Display Issam Bhar's card 
photo_path_issam = current_directory / "data" / "card" / "photos" / "issam_bhar.jpg"
if photo_path_issam.exists():
    st.image(photo_path_issam, caption="Issam Bhar", width=200)
    st.markdown("""
    <div class="card">
        <h4>Issam Bhar</h4>
        <p>Issam Bhar was a journalist for Al-Aqsa TV and was killed during an Israeli airstrike on a dangerous assignment. He was killed Oct. 17, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_ibrahim}")

# Display Jamal Al-Faqaawi's card
photo_path_jamal = current_directory / "data" / "card" / "photos" / "jamal_al-faqaawi.jpg"
if photo_path_jamal.exists():
    st.image(photo_path_jamal, caption="Jamal Al-Faqaawi", width=200)
    st.markdown("""
    <div class="card">
        <h4>Jamal Al-Faqaawi</h4>
        <p>Jamal Al-Faqaawi was a journalist for the Mithaq Media Foundation. He was killed during an Israeli strike that struck his home. He was killed Oct. 25, 2023. </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_jamal}")

# Display Khalil Abu Aathra's card
photo_path_khalil = current_directory / "data" / "card" / "photos" / "khalil_abu_aathra.jpg"
if photo_path_khalil.exists():
    st.image(photo_path_khalil, caption="Khalil Abu Aathra", width=200)
    st.markdown("""
    <div class="card">
        <h4>Khalil Abu Aathra</h4>
        <p>Khalil Abu Aathra was a journalist who worked for Al-Aqsa TV. He was killed with his brother during an Israeli airstrike. He was killed Oct. 19, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_khalil}")

# Display Mohammad Balousha's card
photo_path_balousha = current_directory / "data" / "card" / "photos" / "mohammad_balousha.jpg"
if photo_path_balousha.exists():
    st.image(photo_path_balousha, caption="Mohammad Balousha", width=200)
    st.markdown("""
    <div class="card">
        <h4>Mohammad Balousha</h4>
        <p>Mohammad Balousha, 38, was a broadcast reporter for Al Mashhad Media who covered human rights and war. He was killed on Dec. 14, 2024.2</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_balousha}")

# Display Mohammad Jarghoun's card
photo_path_jarghoun = current_directory / "data" / "card" / "photos" / "mohammad_jarghoun.jpg"
if photo_path_jarghoun.exists():
    st.image(photo_path_jarghoun, caption="Mohammad Jarghoun", width=200)
    st.markdown("""
    <div class="card">
        <h4>Mohammad Jarghoun</h4>
        <p>Mohammad Jarghoun was a journalist with Snart Media who was killed on the Gaza Strip in Rafah city. He was killed on Oct. 7, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_jarghoun}")

# Display Mohammed Al-Salhi's card
photo_path_salhi = current_directory / "data" / "card" / "photos" / "mohammed_al-salhi.jpg"
if photo_path_salhi.exists():
    st.image(photo_path_salhi, caption="Mohammed Al-Salhi", width=200)
    st.markdown("""
    <div class="card">
        <h4>Mohammed Al-Salhi</h4>
        <p>Mohammed Al-Salhi was a photojournalist for the Fourth Authority news agency. He was a war photojournalist that was killed near a Palestinian refugee camp. He was killed Oct. 7, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_salhi}")

# Display Mohammed Ali's card
photo_path_ali = current_directory / "data" / "card" / "photos" / "mohammed_ali.jpg"
if photo_path_ali.exists():
    st.image(photo_path_ali, caption="Mohammed Ali", width=200)
    st.markdown("""
    <div class="card">
        <h4>Mohammed Ali</h4>
        <p>Mohammed Ali was a broadcast reporter for Al-Shabab Radio. He was killed in an airstrike near the Gaza Strip. He died Oct. 20, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_ali}")

# Display Mohammed Imad Labad's card
photo_path_labad = current_directory / "data" / "card" / "photos" / "mohammed_imad_labad.jpg"
if photo_path_labad.exists():
    st.image(photo_path_labad, caption="Mohammed Imad Labad", width=200)
    st.markdown("""
    <div class="card">
        <h4>Mohammed Imad Labad</h4>
        <p>Mohammed Imad Labad was a journalist for Al Resalah and was killed during an Israeli airstrike. He was killed Oct. 23, 2023.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image not found: {photo_path_labad}")
