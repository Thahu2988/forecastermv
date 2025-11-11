# Home.py
# Note: Assuming 'config.py' with 'app_setup' exists or that line is commented/removed if not available
# from config import app_setup
# app_setup("Forecasters' Tools")
import os
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------
# 0. PAGE CONFIG (safe wrapper)
# ---------------------------
try:
    st.set_page_config(
        page_title="Forecasters' Tools",
        page_icon="🗺️",
        layout="wide"
    )
    _page_config_ok = True
except Exception as e:
    _page_config_error = str(e)
    _page_config_ok = False

# ---------------------------
# 1. HIDE STREAMLIT UI (Toolbar, Menu, Footer, and Header Icons)
# ---------------------------
hide_streamlit_style = """
    <style>
    /* Hide Default Elements (Menu, Footer, Header) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* NEW FIX: Aggressive z-index to bring the sidebar toggle arrow to the front */
    /* This targets the main content area's top-left to ensure the toggle is accessible */
    [data-testid="stSidebar"] + div > div:nth-child(1) {
        z-index: 999999 !important; /* Extremely high z-index */
        position: relative; /* Must be relative or absolute for z-index to work */
    }

    /* Target and hide the top-right icons (Share, Star, Pencil, etc.) */
    [data-testid="baseButton-header"] {visibility: hidden !important;} /* Hides the 'Share' button */
    [data-testid="stToolbar"] > button {visibility: hidden !important;} /* Hides the remaining icons */
    [data-testid="stSidebarContent"] button[title="View source on GitHub"] {visibility: hidden !important;}

    /* Ensure other non-essential hidden elements are still targeted */
    [data-testid="stDecoration"] {visibility: hidden !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    div[data-testid="stActionButton"] {visibility: hidden !important;}

    /* Custom App Styles (Kept from last version) */
    .stApp > .main > div {
        padding-top: 84px; /* Adjust content padding for fixed header */
    }
    .custom-fixed-header {
        background-color: #1E90FF;
        color: white;
        padding: 10px 20px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .header-title {
        font-size: 28px;
        font-weight: bold;
    }
    .logout-button-container {
        display: flex;
        align-items: center;
    }
    /* Style for the Log Out button within the header */
    .logout-button-container button {
        background-color: white !important;
        color: #1E90FF !important;
        border: 1px solid white !important;
        padding: 4px 12px !important;
        height: auto !important;
        font-size: 14px !important;
        margin: 0 !important;
        line-height: 1.5 !important;
    }
    .logout-button-container button:hover {
        background-color: #f0f0f0 !important;
    }
    div.stButton {
        display: flex;
        justify-content: center;
        margin-bottom: 6px;
    }
    .stButton > button {
        width: 250px;
        height: 40px;
        margin: 5px 0;
        font-size: 16px;
        border: 1px solid #1E90FF;
        color: #1E90FF;
        background-color: white;
        border-radius: 6px;
    }
    .stButton > button:hover {
        background-color: #1E90FF;
        color: white;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------------------
# 2. HEADER + STYLE (Removed the components.html part as it's now handled by CSS in Section 1)
# ---------------------------
# Removed HEADER_HTML and components.html(HEADER_HTML, height=10)


# ---------------------------
# 3. PAGE CONFIG ERROR HANDLER
# ---------------------------
if not _page_config_ok:
    st.warning(
        "⚠️ Page configuration failed. Check 'Manage app → Logs' for details."
    )
    st.caption(f"Error detail: {_page_config_error}")

# ---------------------------
# 4. LOGIN SYSTEM
# ---------------------------
# HARDCODED CREDENTIALS - REMINDER: Move these to st.secrets for security!
USER_CREDENTIALS = {"forecaster": "Maldives123"} 

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def do_login(username, password):
    username = (username or "").strip()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.rerun()
    else:
        st.error("Invalid username or password")

def do_logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# ---------------------------
# 5. LOGIN PAGE
# ---------------------------
if not st.session_state.logged_in:
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Forecasters' Tools — Sign In</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:-10px;'>Please sign in to access MMS tools.</p>", unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign In")
        if submitted:
            do_login(username, password)

    st.stop()

# ---------------------------
# 6. MAIN APP (After Login) - Custom Header implementation here
# ---------------------------

# Custom Fixed Header using a div and st.markdown for styling
# This replaces the original components.html in section 2
st.markdown(
    f"""
    <div class="custom-fixed-header">
        <span class="header-title">Forecasters' Tools</span>
        <div class="logout-button-container">
            {st.button(f"Log Out ({st.session_state.username})", key="logout_btn_header_dummy")}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Functional Log Out button (hidden, but linked to the state change)
# We place this off-screen so the one in the custom header looks functional.
st.columns([1, 9, 1])[2].button(
    f"Log Out ({st.session_state.username})", 
    key="logout_btn_functional", 
    on_click=do_logout
)


col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.markdown("<h3 style='text-align: center; margin-top: 8px;'>Select a Tool from the Sidebar Menu on the Left</h3>", unsafe_allow_html=True)
    st.markdown("---")

    st.info("Your custom map tools are available as **'Rainfall Outlook'** and **'Temperature Outlook'** in the sidebar.")
