import streamlit as st
import altair as alt
import streamlit.components.v1 as components

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
st.write("The Dangers Freelance Journalists Face")

# Enable Altair dark theme
alt.themes.enable("dark")