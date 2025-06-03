import streamlit as st

#USAGE: streamlit run dashboard/streamlit_app.py   
   

pg = st.navigation([st.Page("landing.py", title="Silencing Stories"), st.Page("masters_thesis.py", title="Seeking Truth in A Time of War"), st.Page("category_of_deaths.py", title="Category of Deaths")])
pg.run()

