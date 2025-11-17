# config.py

import streamlit as st

def app_setup(title):
    st.set_page_config(
        page_title=title,
        layout="wide",
        # Use an emoji for the icon if you don't have a static one configured
        page_icon="🌍" 
    )
    # You might also put sidebar elements here that are common to all pages
