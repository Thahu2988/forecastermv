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

with col1:
    st.header("💧 Rainfall Analysis")
    st.info("View maps and charts related to rainfall data.")
    if st.button("Go to Rainfall", key="btn_rainfall", use_container_width=True):
        # ✅ Correct: Matches pages/Rainfall_Outlook.py without the extension
        st.switch_page("Rainfall_Outlook") 

with col2:
    st.header("🌡️ Temperature Analysis")
    st.info("Explore global or local temperature variations and trends.")
    if st.button("Go to Temperature", key="btn_temp", use_container_width=True):
        # ❌ FIX: Removed the incorrect '.py' extension. 
        # Assumes the file in pages/ is named 'Temperature_Outlook.py'
        st.switch_page("Temperature_Outlook") 

with col3:
    st.header("📞 Viber CST Analysis")
    st.info("Visualize data related to Viber communication traffic.")
    if st.button("Go to Viber CST", key="btn_viber", use_container_width=True):
        # Assumes the file in pages/ is named 'viber_cst.py'
        st.switch_page("viber_cst") 

st.divider()
