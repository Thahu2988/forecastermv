# Home.py

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
# import all other necessary libraries here...

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
# 2. AUTHENTICATION SETUP (Can be after st.set_page_config)
# ------------------------------------------------

# WARNING: Use your actual generated hash here
hashed_passwords = ['$2b$12$ABCDEFGHIJKLMNO.PQRSTUVWXYZ.EXAMPLE.HASH.DO.NOT.USE'] 

authenticator = stauth.Authenticate(
    names=['MMS Forecaster'],
    usernames=['metmdv'], # Corresponds to metmdv@gmail.com's user
    passwords=hashed_passwords,
    cookie_name='forecaster_cookie',
    key='random_auth_key',
    cookie_expiry_days=30
)

# --- Check Login Status ---
name, authentication_status, username = authenticator.login('Login', 'main')

# ------------------------------------------------
# 3. RENDER APP CONTENT BASED ON LOGIN STATUS
# ------------------------------------------------

if authentication_status:
    # ... Your existing CSS and main content rendering code goes here ...
    # ... starting from st.markdown("""<style>... ...

# ------------------------------------------------
# 4. HANDLE AUTHENTICATION FAILURES (Same as before)
# ------------------------------------------------
elif authentication_status is False:
    st.error('Username/password is incorrect')
    # Note: We can't change the page_title here, as set_page_config is already called

elif authentication_status is None:
    st.warning('Please enter your username and password')
    # Note: We can't change the page_title here
