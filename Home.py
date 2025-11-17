# Home.py (TEMPORARY TEST SCRIPT)
# Home.py
from config import app_setup 
app_setup("Geospatial Data Explorer") # Must be the very first lines!
# ... rest of the imports and code
import streamlit as st
from config import app_setup 

# --- Configuration ---
app_setup("Geospatial Data Explorer") 

# --- Home Page Content ---
st.title("🌍 Geospatial Data Explorer - Navigation Test")
st.markdown("Click the 'Navigation Test' tab and the button to verify page switching works.")
st.divider()

# --- Navigation using Tabs ---
# Use the same tab structure, but link the first tab to the safe test page
tab1, tab2, tab3 = st.tabs([
    "🧪 Navigation Test",   # Renamed for clarity
    "🌡️ Temperature Analysis (Disabled)", 
    "📞 Viber CST Analysis (Disabled)"
])

# Tab 1: Navigation Test
with tab1:
    st.info("Click the button below to switch to the safe 'Test_Page1'.")
    if st.button("Go to Test Page 1", key="btn_test_page", type="primary", use_container_width=True):
        # We switch to the simple page that is guaranteed not to crash.
        st.switch_page("Test_Page1") 

# Tab 2 & 3: Disabled to avoid crashing pages
with tab2:
    st.warning("Feature disabled for testing.")

with tab3:
    st.warning("Feature disabled for testing.")

st.divider()

