# Home.py

import streamlit as st

# ------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="Forecasters' Tools",
    page_icon="🗺️",
    layout="wide"
)

# Hide Streamlit default menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 2. SIMPLE AUTHENTICATION SYSTEM
# ------------------------------------------------------------
# Demo credentials (replace with secure backend later)
USER_CREDENTIALS = {
    "forecaster": "mms123"
}

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def login():
    """Handles user login"""
    username = st.session_state["login_user"]
    password = st.session_state["login_pass"]
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login successful! Loading tools...")
        st.rerun()
    else:
        st.error("Invalid username or password")

def logout():
    """Handles logout"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# ------------------------------------------------------------
# 3. LOGIN PAGE (if not logged in)
# ------------------------------------------------------------
if not st.session_state.logged_in:
    st.markdown(
        """
        <div style='text-align:center; padding-top:100px;'>
            <h2>🔒 Forecasters' Tools Login</h2>
            <p>Please sign in with your credentials to access MMS tools.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("login_form", clear_on_submit=False):
        st.text_input("Username", key="login_user")
        st.text_input("Password", type="password", key="login_pass")
        submitted = st.form_submit_button("Sign In", use_container_width=True)
        if submitted:
            login()
    st.stop()  # Stop execution until logged in

# ------------------------------------------------------------
# 4. MAIN APPLICATION (after login)
# ------------------------------------------------------------

# Inject Custom CSS for Header and Buttons
st.markdown(
    """
    <style>
    /* HEADER BAR */
    .main-header {
        background-color: #1E90FF;
        color: white;
        padding: 10px 0;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .logout-link {
        position: absolute;
        right: 20px;
        top: 15px;
        font-size: 14px;
        color: white;
        text-decoration: none;
    }
    .logout-link:hover {
        text-decoration: underline;
    }
    /* Push main content down */
    .stApp > .main > div {
        padding-top: 80px;
    }
    /* BUTTON STYLE */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-bottom: 5px;
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
    """,
    unsafe_allow_html=True
)

# HEADER BAR WITH LOGOUT
st.markdown(
    f"""
    <div class="main-header">
        Forecasters' Tools 
        <a href="#" class="logout-link" onClick="window.location.reload();">Log Out ({st.session_state.username})</a>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# 5. MAIN CONTENT
# ------------------------------------------------------------
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Select a Tool from the Sidebar Menu on the Left</h3>", unsafe_allow_html=True)
    st.markdown("---")

    # Example Buttons (replace with navigation logic later)
    st.button("Tide Chart")
    st.button("Alert Graphic")
    st.button("Forecast Graphic")
    st.button("Weekend Forecast")
    st.button("Satellite Image")
    st.button("Forecast App (Testing)")
    st.button("Weather News")

    st.markdown("---")
    st.info("Your custom map tools are now available as **'Rainfall Outlook'** and **'Temperature Outlook'** in the sidebar menu.")

# ------------------------------------------------------------
# 6. LOGOUT BUTTON (optional footer version)
# ------------------------------------------------------------
st.markdown("<br><center><a href='#' onClick='window.location.reload();' style='color:#1E90FF;'>🔓 Log Out</a></center>", unsafe_allow_html=True)
