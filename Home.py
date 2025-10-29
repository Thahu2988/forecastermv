# Home.py

import streamlit as st

st.set_page_config(
    page_title="Forecasters' Tools",
    page_icon="🗺️",
    layout="wide",
    # CRITICAL: Hides the hamburger menu (View App, Settings, About) 
    menu_items={'About': 'Developed by Thahumeena from Maldives Meteorological Service (MMS)', 
                'Get Help': None, 
                'Report a bug': None},
    # CRITICAL: Hides the GitHub Icon, Edit Icon, and Star Icon toolbar
    show_toolbar_by_default=False 
)

# 2. Inject Custom CSS for the Blue Header Bar and Button Styling
st.markdown(
    """
    <style>
    /* CUSTOM BLUE HEADER BAR */
    .main-header {
        background-color: #1E90FF; /* Bright Blue */
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
    
    /* Push main content down to account for the fixed header */
    /* Targeting specific container classes to push content down */
    .st-emotion-cache-1g8i5u7, .st-emotion-cache-6qob1r, .st-emotion-cache-1y4pm5r {
        padding-top: 80px; 
    }
    .logout-link {
        position: absolute;
        right: 20px;
        top: 15px;
        font-size: 14px;
        color: white;
        text-decoration: none;
    }
    /* CUSTOM BUTTON STYLING (Centered and Stacked) */
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

# Renders the fixed blue header bar with the title and a placeholder Logout link
st.markdown('<div class="main-header">Forecasters\' Tools <a href="#" class="logout-link">Log Out</a></div>', unsafe_allow_html=True)

# Main Page Content (Below the Header)
# Use columns to center the buttons
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Select a Tool from the Sidebar Menu on the Left</h3>", unsafe_allow_html=True)
    st.markdown("---")

    # Placeholder buttons matching the UI image
    st.button("Forecast Graphic")
    st.button("Satellite Image")
    st.button("Weather News")
    
    st.markdown("---")
    # This info message guides the user to the pages folder scripts
    st.info("Your custom map tools are now available as **'Rainfall Outlook'** and **'Temperature Outlook'** in the Streamlit sidebar menu.")

