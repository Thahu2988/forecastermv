# Home.py
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------
# 1. PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Forecasters' Tools",
    page_icon="🗺️",
    layout="wide"
)

# ---------------------------
# 2. CSS + HEADER (via components.html to avoid unsafe_allow_html)
# ---------------------------
# Using components.html avoids problems with deprecated/changed st.markdown kwargs.
HEADER_HTML = """
<style>
/* Hide default Streamlit menu + footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* MAIN HEADER */
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
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

/* Logout link (position inside header) */
.logout-link {
    position: absolute;
    right: 20px;
    top: 12px;
    font-size: 14px;
    color: white;
    text-decoration: none;
}
.logout-link:hover { text-decoration: underline; }

/* Push main content down to account for the fixed header */
.stApp > .main > div {
    padding-top: 84px;
}

/* Centered stacked buttons styling */
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

<div class="main-header" id="mainHeader">
  Forecasters' Tools
  <!-- the logout link is rendered and handled from Python side; this is just a visual anchor -->
  <span class="logout-link" id="logoutAnchor"></span>
</div>
"""

# Inject header and CSS (height small so it doesn't take large space)
components.html(HEADER_HTML, height=10)

# ---------------------------
# 3. SIMPLE AUTH (session state)
# ---------------------------
# Demo credentials - change to your secure backend when ready
USER_CREDENTIALS = {"forecaster": "mms123"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def do_login(username: str, password: str):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        # Rerun to load main UI
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

def do_logout():
    # Clear only the auth-related items to preserve other state if needed
    st.session_state.logged_in = False
    st.session_state.username = ""
    # Rerun to show login page
    st.experimental_rerun()

# ---------------------------
# 4. LOGIN PAGE
# ---------------------------
if not st.session_state.logged_in:
    # Center the login box vertically using empty space (simple approach)
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center;'>🔒 Forecasters' Tools — Sign In</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:-10px;'>Please sign in to access MMS tools.</p>", unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username", key="form_username")
        password = st.text_input("Password", type="password", key="form_password")
        submitted = st.form_submit_button("Sign In")
        if submitted:
            do_login(username.strip(), password)

    # Helpful demo credentials note (remove in production)
    st.info("Demo credentials — Username: `forecaster`  Password: `mms123`")

    # Stop further execution until logged in
    st.stop()

# ---------------------------
# 5. MAIN APP AFTER LOGIN
# ---------------------------

# Render a small logout button at top-right by showing a link-like button in the layout.
# (We can't directly hook the HTML logoutAnchor link to Python easily, so show a button.)
header_cols = st.columns([1, 9, 1])
with header_cols[2]:
    if st.button(f"Log Out ({st.session_state.username})"):
        do_logout()

# Main content layout (center column for buttons)
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.markdown("<h3 style='text-align: center; margin-top: 8px;'>Select a Tool from the Sidebar Menu on the Left</h3>", unsafe_allow_html=True)
    st.markdown("---")

    # The buttons below are placeholders — connect them to pages or callbacks as you need.
    if st.button("Tide Chart"):
        st.info("Tide Chart clicked — wire this to a page or callback.")
    if st.button("Alert Graphic"):
        st.info("Alert Graphic clicked — wire this to a page or callback.")
    if st.button("Forecast Graphic"):
        st.info("Forecast Graphic clicked — wire this to a page or callback.")
    if st.button("Weekend Forecast"):
        st.info("Weekend Forecast clicked — wire this to a page or callback.")
    if st.button("Satellite Image"):
        st.info("Satellite Image clicked — wire this to a page or callback.")
    if st.button("Forecast App (Testing)"):
        st.info("Forecast App (Testing) clicked — wire this to a page or callback.")
    if st.button("Weather News"):
        st.info("Weather News clicked — wire this to a page or callback.")

    st.markdown("---")
    st.info("Your custom map tools are available as **'Rainfall Outlook'** and **'Temperature Outlook'** in the sidebar menu (add them under pages/ or via sidebar components).")

# Optional: small footer logout link
st.markdown("<br><center><a href='#' style='color:#1E90FF;' onclick='window.location.reload();'>🔓 Log Out</a></center>", unsafe_allow_html=True)
