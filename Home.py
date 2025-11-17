# Home.py
# Home.py
import streamlit as st
from config import app_setup # <--- This line must succeed
app_setup("Geospatial Data Explorer") 
# ... rest of the code ...
import streamlit as st
from config import app_setup # Import your shared setup function

# --- Configuration ---
app_setup("Geospatial Data Explorer") # Applies your custom setup and title

# --- Home Page Content and Navigation ---
st.title("🌍 Geospatial Data Explorer")

st.markdown("""
Welcome to the Geospatial Data Explorer. Use the links below or the **sidebar navigation** to access different analyses.
""")

st.divider()

col1, col2, col3 = st.columns(3)

# Use the corrected dot notation for navigation: 'pages.filename'
with col1:
    st.header("💧 Rainfall Analysis")
    st.info("View maps and charts related to rainfall data.")
    if st.button("Go to Rainfall", key="btn_rainfall", use_container_width=True):
        st.switch_page("pages.rainfall") # ✅ Corrected path

with col2:
    st.header("🌡️ Temperature Analysis")
    st.info("Explore global or local temperature variations and trends.")
    if st.button("Go to Temperature", key="btn_temp", use_container_width=True):
        st.switch_page("pages.temperature") # ✅ Corrected path

with col3:
    st.header("📞 Viber CST Analysis")
    st.info("Visualize data related to Viber communication traffic.")
    if st.button("Go to Viber CST", key="btn_viber", use_container_width=True):
        st.switch_page("pages.viber_cst") # ✅ Corrected path

st.divider()

