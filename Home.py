# ---------------------------
# 1. HIDE STREAMLIT UI (Revised to ensure sidebar toggle is visible)
# ---------------------------
hide_streamlit_style = """
    <style>
    /* Hide Default Elements (Menu, Footer, Header) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* FIX: Aggressively elevate the Sidebar and its toggle container */
    
    /* 1. Ensure the sidebar itself is highly elevated */
    [data-testid="stSidebar"] {
        z-index: 999999 !important; 
    }
    
    /* 2. Elevate the container that holds the toggle icon */
    [data-testid="stDecoration"] {
        z-index: 999999 !important;
        visibility: visible !important; /* Ensure it's not accidentally hidden */
        /* Also target the default streamlit header which often contains the toggle */
        background-color: transparent !important;
        height: 0 !important;
    }
    
    /* 3. Lower the main content container relative to the custom fixed header (z-index: 1000), 
          forcing the sidebar toggle (which is outside of the main content) to appear on top. */
    .stApp > header {
        z-index: 999 !important; 
    }

    /* Hide only the Share button, and skip hiding other toolbar icons */
    [data-testid="baseButton-header"] {visibility: hidden !important;}

    /* Ensure other non-essential hidden elements are still targeted */
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    div[data-testid="stActionButton"] {visibility: hidden !important;}

    /* Custom App Styles (Keep z-index at 1000 for the fixed header) */
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
        z-index: 1000; /* Custom Header z-index */
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
