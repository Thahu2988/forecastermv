# pages/Test_Page1.py

import streamlit as st
from config import app_setup

# Note: We must call app_setup on the page for a multi-page app
app_setup("Test Page") 

st.title("✅ Test Page 1 Success!")
st.success("This page loaded without crashing. This confirms the multi-page app structure is correct.")
st.markdown("The navigation link from the Home page tab is working properly.")