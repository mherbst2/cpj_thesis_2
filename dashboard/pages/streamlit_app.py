import streamlit as st

#USAGE: streamlit run dashboard/streamlit_app.py   
   

pg = st.navigation([st.Page("landing.py", title="Homepage"), st.Page("masters_thesis.py", title="Seeking Truth in A Time of War"), st.Page("war_in_gaza.py", title="The War in Gaza and the Press"), st.Page("freelance_journ.py", title="Freelance Journalists"), st.Page("journ_finder.py", title="Journalist Finder")],)
pg.run()

