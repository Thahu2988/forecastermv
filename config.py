# config.py — shared setup for all pages
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
    [data-testid="baseButton-header"] {visibility: hidden !important;} /* Hides the 'Share' button */
    [data-testid="stToolbar"] > button {visibility: hidden !important;} /* Hides the other icons in the toolbar */
    [data-testid="stSidebarContent"] button[title="View source on GitHub"] {visibility: hidden !important;}

    /* Ensure other non-essential hidden elements are still targeted */
    [data-testid="stDecoration"] {visibility: hidden !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    div[data-testid="stActionButton"] {visibility: hidden !important;}
    
    /* The line below is commented out to ensure the sidebar toggle remains visible: */
    /* [data-testid="stToolbar"] {visibility: hidden !important;} */
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
