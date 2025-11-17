# Home.py
import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="My Geospatial Data App",
    page_icon="🌍",
    layout="wide"
)

# --- 1. Hide the Streamlit Menu/Toolbar (Addresses your request) ---
# This CSS snippet targets the specific elements that typically contain the "Share/Star/Settings" menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# 

# --- 2. Home Page Content and Navigation ---
st.title("🌍 Geospatial Data Explorer")

st.markdown("""
Welcome to the Geospatial Data Explorer. Use the links below or the **sidebar navigation** to access different analyses.
""")

st.divider()

col1, col2, col3 = st.columns(3)

# Note: st.switch_page uses ONLY the filename (e.g., "rainfall.py")
# when navigating to a file inside the 'pages' directory.

with col1:
    st.header("💧 Rainfall Analysis")
    st.info("View maps and charts related to rainfall data.")
    if st.button("Go to Rainfall", key="btn_rainfall", use_container_width=True):
        st.switch_page("rainfall.py") # CORRECTED path

with col2:
    st.header("🌡️ Temperature Analysis")
    st.info("Explore global or local temperature variations and trends.")
    if st.button("Go to Temperature", key="btn_temp", use_container_width=True):
        st.switch_page("temperature.py") # CORRECTED path

with col3:
    st.header("📞 Viber CST Analysis")
    st.info("Visualize data related to Viber communication traffic.")
    if st.button("Go to Viber CST", key="btn_viber", use_container_width=True):
        st.switch_page("viber_cst.py") # CORRECTED path

st.divider()

