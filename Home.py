# Home.py

import streamlit as st
from config import app_setup # Import your shared setup function

# --- Configuration ---
# Sets up the page title, icon, layout, and custom CSS via config.py
app_setup("Geospatial Data Explorer") 

# --- Home Page Content ---
st.title("🌍 Geospatial Data Explorer")

st.markdown("""
Welcome to the Geospatial Data Explorer. Use the links below or the **sidebar navigation** to access different analyses.
""")

st.divider()

# --- Navigation Buttons ---
col1, col2, col3 = st.columns(3)

# The switch_page call MUST match the filename in the pages/ directory 
# (Rainfall_Outlook.py) exactly, excluding the .py extension.
with col1:
    st.header("💧 Rainfall Analysis")
    st.info("View maps and charts related to rainfall data.")
    if st.button("Go to Rainfall", key="btn_rainfall", use_container_width=True):
        st.switch_page("Rainfall_Outlook") # ✅ Corrected to match the filename

with col2:
    st.header("🌡️ Temperature Analysis")
    st.info("Explore global or local temperature variations and trends.")
    if st.button("Go to Temperature", key="btn_temp", use_container_width=True):
        st.switch_page("temperature") # Assuming this file is pages/temperature.py

with col3:
    st.header("📞 Viber CST Analysis")
    st.info("Visualize data related to Viber communication traffic.")
    if st.button("Go to Viber CST", key="btn_viber", use_container_width=True):
        st.switch_page("viber_cst") # Assuming this file is pages/viber_cst.py

st.divider()
