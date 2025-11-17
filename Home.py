# Home.py

import streamlit as st
from config import app_setup 

# --- Configuration ---
app_setup("Geospatial Data Explorer") 

# --- Home Page Content ---
st.title("🌍 Geospatial Data Explorer")

st.markdown("""
Welcome to the Geospatial Data Explorer. Select a tool below or use the sidebar navigation.
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
    st.info("View and adjust the Maximum Rainfall Outlook Map.")
    if st.button("Go to Rainfall Map", key="btn_rainfall_tab", type="primary", use_container_width=True):
        # Correct function name and page file name
        st.switch_page("Rainfall_Outlook") 

# Tab 2: Temperature Analysis
with tab2:
    st.info("Explore global or local temperature variations and trends.")
    if st.button("Go to Temperature Tool", key="btn_temp_tab", use_container_width=True):
        # Correct function name and assumed page file name
        st.switch_page("Temperature_Outlook") 

# Tab 3: Viber CST Analysis
with tab3:
    st.info("Visualize data related to Viber communication traffic.")
    if st.button("Go to Viber CST Tool", key="btn_viber_tab", use_container_width=True):
        # Correct function name and assumed page file name
        st.switch_page("viberfcst_final") 

st.divider()
