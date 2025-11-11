import streamlit as st 

# ---------------------------
# 1. HIDE STREAMLIT UI & PUSH CONTENT DOWN
# ---------------------------
hide_streamlit_style = """
    <style>
    /* HIDE DEFAULT STREAMLIT ELEMENTS */
    /* Hide the hamburger/ellipsis menu in the top right */
    #MainMenu {visibility: hidden !important;} 
    /* Hide the footer ("Made with Streamlit") */
    footer {visibility: hidden !important;}
    /* Hide the default Streamlit header/toolbar (which contains the Share button) */
    .stApp > header {visibility: hidden !important;} 
    
    /* PUSH MAIN CONTENT DOWN */
    /* This rule targets the main container where your app content lives. 
       Adjust the 'padding-top' value to push the content down 
       and hide the default top bar behind your custom header or just into the margin. 
       If you are using a custom header, this padding should match the custom header's height. 
       We use a large value here (e.g., 50px) to ensure the top bar is hidden. */
    .stApp > div:first-child > section {
        padding-top: 50px !important;
    }
    
    /* ENSURE SIDEBAR TOGGLE IS VISIBLE & ON TOP */
    /* The sidebar toggle is part of the stDecoration container. 
       We ensure it's visible and highly elevated. */
    [data-testid="stDecoration"] {
        visibility: visible !important;
        z-index: 999999 !important; /* Keep it on top of everything */
    }

    /* Clean up residual custom fixed header styles if you are no longer using them */
    /* If you still use the 'custom-fixed-header' you must keep these rules */
    .custom-fixed-header {
        /* ... existing custom header styles ... */
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        /* ... other styles ... */
    }
    
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ... rest of your Streamlit app code ...
