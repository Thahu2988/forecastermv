# Home.py

import streamlit as st
# Imports for authentication
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ------------------------------------------------
# 1. PAGE CONFIGURATION (MUST BE FIRST ST. COMMAND)
# ------------------------------------------------
st.set_page_config(
    page_title="Forecasters' Tools",
    page_icon="🗺️",
    layout="wide",
    menu_items={'About': 'Developed by Maldives Meteorological Service (MMS)', 
                'Get Help': None, 
                'Report a bug': None},
    show_toolbar_by_default=False 
)


# ------------------------------------------------
# 2. AUTHENTICATION SETUP 
# ------------------------------------------------

# ⚠️ WARNING: Use your actual generated hash here
# This example uses 'metmdv' as the username (corresponding to the email metmdv@gmail.com)
# The password must be HASHED.
hashed_passwords = ['$2b$12$ABCDEFGHIJKLMNO.PQRSTUVWXYZ.EXAMPLE.HASH.DO.NOT.USE'] 

authenticator = stauth.Authenticate(
    names=['MMS Forecaster'],
    usernames=['metmdv'],
    passwords=hashed_passwords,
    cookie_name='forecaster_cookie',
    key='random_auth_key',
    cookie_expiry_days=30
)

# --- Check Login Status ---
# Logs the user in via a form rendered in the main area of the page
name, authentication_status, username = authenticator.login('Login', 'main')

# ------------------------------------------------
# 3. RENDER APP CONTENT BASED ON LOGIN STATUS
# ------------------------------------------------

if authentication_status:
    # 3A. Inject Custom CSS for Header/Buttons and UI Hiding
    st.markdown(
        """
        <style>
        /* Hide the specific Streamlit 'Share' button/widget */
        .st-emotion-cache-1jm69yr { 
            display: none !important;
        }

        /* CUSTOM BLUE HEADER BAR */
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
        
        /* Push main content down */
        .st-emotion-cache-1g8i5u7, .st-emotion-cache-6qob1r, .st-emotion-cache-1y4pm5r {
            padding-top: 80px; 
        }
        
        /* Logout Link/Button Placement */
        #logout-button {
            position: absolute;
            right: 20px;
            top: 15px;
        }

        /* CUSTOM BUTTON STYLING */
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
        }
        .stButton > button:hover {
            background-color: #1E90FF;
            color: white;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # 3B. RENDER APP CONTENT
    # Render the fixed blue header bar with the title and the Logout button
    st.markdown('<div class="main-header">Forecasters\' Tools</div>', unsafe_allow_html=True)
    authenticator.logout('Log Out', 'fixed', key='logout-button')


    # Main Page Content (Below the Header)
    col_left, col_center, col_right = st.columns([1, 2, 1])

    with col_center:
        st.markdown(f"**Welcome, {name}!**", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Select a Tool from the Sidebar Menu on the Left</h3>", unsafe_allow_html=True)
        st.markdown("---")

        # ONLY THE REQUESTED BUTTONS
        st.button("Rainfall Probablity")
        st.button("Temperature Probability")
        st.button("Forecast Graphic")
        st.button("Satellite Image")
        
        st.markdown("---")
        st.info("The map tools, 'Rainfall Outlook' and 'Temperature Outlook', are available in the sidebar menu.")

# ------------------------------------------------
# 4. HANDLE AUTHENTICATION FAILURES
# ------------------------------------------------
elif authentication_status is False:
    st.error('Username/password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password')
