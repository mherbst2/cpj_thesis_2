import streamlit as st

#USAGE: streamlit run dashboard/streamlit_app.py   
   

pg = st.navigation([st.Page("landing.py", title="Landing Page"), st.Page("war_in_gaza.py", title="War in Gaza"), st.Page("category_of_deaths.py", title="Category of Deaths")])
pg.run()

