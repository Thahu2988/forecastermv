# Home.py

import streamlit as st
from config import app_setup # Import your shared setup function

# --- Configuration ---
app_setup("Geospatial Data Explorer") 

# --- Home Page Content ---
st.title("🌍 Geospatial Data Explorer")

st.markdown("""
Welcome to the Geospatial Data Explorer. Select a tool below to begin your analysis.
""")

st.divider()

# --- Navigation using Tabs ---
tab1, tab2, tab3 = st.tabs([
    "💧 Rainfall Analysis", 
    "🌡️ Temperature Analysis", 
    "📞 Viber CST Analysis"
])

# Tab 1: Rainfall Analysis
with tab1:
    st.info("Click the button below to view and adjust the Rainfall Outlook Map.")
    if st.button("Go to Rainfall Map", key="btn_rainfall_tab", type="primary", use_container_width=True):
        # Correct function and correct filename
        st.switch_page("Rainfall_Outlook") 

# Tab 2: Temperature Analysis
with tab2:
    st.info("Click the button below to explore temperature variations and trends.")
    if st.button("Go to Temperature Tool", key="btn_temp_tab", use_container_width=True):
        # Correct function and correct filename
        st.switch_page("Temperature_Outlook") 

# Tab 3: Viber CST Analysis
with tab3:
    st.info("Click the button below to visualize Viber communication traffic data.")
    if st.button("Go to Viber CST Tool", key="btn_viber_tab", use_container_width=True):
        # 🔥 FIX: Corrected to match the actual filename: viberfcst_final.py
        st.switch_page("viberfcst_final") 

st.divider()
