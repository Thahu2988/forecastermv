# config.py

import streamlit as st

def app_setup(page_title="Forecasters' Tools"):
    """
    Sets the page configuration and applies custom CSS to hide Streamlit 
    default UI elements while preserving the sidebar toggle arrow.
    """
    # 1. PAGE CONFIG
    try:
        st.set_page_config(page_title=page_title, page_icon="🗺️", layout="wide")
    except Exception:
        # Prevents errors if st.set_page_config is called multiple times 
        # (e.g., in development environment)
        pass

    # 2. HIDE STREAMLIT UI (Revised to keep the sidebar toggle visible)
    hide_style = """
    <style>
    /* Hide the default Streamlit menu, footer, and header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* **FIX:** Hide top-right icons (Share, Settings, etc.) but avoid hiding the
        entire toolbar, which contains the essential sidebar toggle arrow. */
    
    /* Hides the 'Share' button */
    [data-testid="baseButton-header"] {visibility: hidden !important;} 
    
    /* Hides the other icons in the toolbar, typically 'Settings' */
    [data-testid="stToolbar"] > button {visibility: hidden !important;} 
    
    /* Hides the 'View source on GitHub' button if present */
    [data-testid="stSidebarContent"] button[title="View source on GitHub"] {visibility: hidden !important;}

    /* Ensure other non-essential hidden elements are still targeted */
    [data-testid="stDecoration"] {visibility: hidden !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    div[data-testid="stActionButton"] {visibility: hidden !important;}
    
    /* The sidebar toggle is usually preserved because we are hiding 
       specific buttons, not the entire toolbar. */
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
