# pages/Rainfall_Outlook.py

# --- Imports and Setup ---
# Assuming app_setup sets st.set_page_config and other initial settings
from config import app_setup 
app_setup("Forecasters' Tools") 

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import box
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import streamlit as st
from io import BytesIO

# --- Caching the expensive data load operation (CRITICAL FIX) ---
@st.cache_data
def load_and_preprocess_data():
    """Loads, clips, and preprocesses the geospatial data. Runs only once."""
    # ⚠️ Use the case that matches your repository files (mixed case)
    # The full filename including the directory structure is used.
    shp = 'data/Atoll_boundary2016.shp' 
    
    try:
        # Load shapefile and project to WGS84
        gdf = gpd.read_file(shp).to_crs(epsg=4326)
    except Exception as e:
        # Raise an exception to be caught by the main script for better error reporting
        raise FileNotFoundError(f"Failed to load geospatial data from {shp}: {e}")
        
    # Clip extent
    bbox = box(71, -1, 75, 7.5)
    gdf = gdf[gdf.intersects(bbox)]

    # Clean missing or invalid atoll names
    gdf['Name'] = gdf['Name'].fillna("Unknown")

    return gdf

# --- Page Title ---
st.title("💧 Maximum Rainfall Outlook Map")
st.markdown("Use the sidebar to adjust the forecasted category and probability for each atoll.")

# --- Data Loading and Preprocessing ---
try:
    # Load data using the cached function
    gdf = load_and_preprocess_data()
except FileNotFoundError as e:
    st.error(f"Error loading map data: {e}")
    # Display the error but continue to allow the app to be debugged.
    st.stop() 

# Ensure unique atoll names
unique_atolls = sorted(gdf['Name'].unique().tolist())

# --- Sidebar Inputs (Atoll Selection) ---

# Editable map title (sidebar)
st.sidebar.write("### ✏️ Map Settings")
map_title = st.sidebar.text_input("Edit Map Title:", "Maximum Rainfall Outlook for OND 2025")

# Categories for each atoll
categories = ['Below Normal', 'Normal', 'Above Normal']

# Sidebar instructions
st.sidebar.write("### Adjust Atoll Categories & Percentages")
st.sidebar.write("Select category and percentage for each atoll:")

# Dictionaries to store selections
selected_categories = {}
selected_percentages = {}

# Sidebar inputs for each unique atoll
for i, atoll in enumerate(unique_atolls):
    # Use columns for a slightly cleaner layout in the sidebar
    col_cat, col_perc = st.sidebar.columns([0.6, 0.4])

    with col_cat:
        selected = st.selectbox(
            f"{atoll} Category", categories, index=1, key=f"{atoll}_cat_{i}", label_visibility="collapsed"
        )
    with col_perc:
        percent = st.slider(
            f"{atoll} %", min_value=0, max_value=100, value=60, step=5, key=f"{atoll}_perc_{i}", label_visibility="collapsed"
        )
    
    selected_categories[atoll] = selected
    selected_percentages[atoll] = percent

# --- Color Mapping and Normalization ---
cmap_below = ListedColormap([
    '#ffffff', '#ffed5c', '#ffb833', '#ff8f00', '#f15c00', '#e20000'
])
cmap_normal = ListedColormap([
    '#ffffff', '#b2df8a', '#6dc068', '#2d933e', '#006a2e', '#014723'
])
cmap_above = ListedColormap([
    '#ffffff', '#c8c8ff', '#a6b6ff', '#8798f0', '#6c7be0', '#3c4fc2'
])

# Bins and normalization
bins = [0, 35, 45, 55, 65, 75, 100]
norm = BoundaryNorm(bins, ncolors=len(bins)-1, clip=True)
tick_positions = [35, 45, 55, 65, 75]
tick_labels = ['35', '45', '55', '65', '75']

# Map selections back to gdf (so all parts of same atoll share same values)
gdf['category'] = gdf['Name'].map(selected_categories)
gdf['prob'] = gdf['Name'].map(selected_percentages)

# --- Plotting Setup ---
fig, ax = plt.subplots(figsize=(12, 10))

# Plot each category with its respective color map
for cat, cmap in zip(['Below Normal', 'Normal', 'Above Normal'],
                     [cmap_below, cmap_normal, cmap_above]):
    subset = gdf[gdf['category'] == cat]
    if not subset.empty:
        subset.plot(
            column='prob', cmap=cmap, norm=norm,
            edgecolor='black', linewidth=0.5, ax=ax
        )

# Axis and title
ax.set_xlim(71, 75)
ax.set_ylim(-1, 7.5)
ax.set_title(map_title, fontsize=18)
ax.set_xlabel("Longitude (°E)", fontsize=14)
ax.set_ylabel("Latitude (°N)", fontsize=14)
ax.set_xticks([71, 72, 73, 74, 75])
ax.set_xticklabels(['71', '72', '73', '74', '75'])
ax.tick_params(labelsize=12)

# Function for colorbars
width = "40%"
height = "2.5%"
start_x = 0.05
start_y = 0.1
spacing = 0.09

def make_cb(ax, cmap, title, offset):
    cax = inset_axes(ax, width=width, height=height, loc='lower left',
                     bbox_to_anchor=(start_x, start_y + offset, 1, 1),
                     bbox_transform=ax.transAxes, borderpad=0)
    cb = colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, boundaries=bins,
                               ticks=tick_positions, spacing='uniform', orientation='horizontal')
    cb.set_ticklabels(tick_labels)
    cax.set_title(title, fontsize=10, pad=6)
    cb.ax.tick_params(labelsize=9, pad=2)

# Rearranged order — Above on top, Normal middle, Below bottom
make_cb(ax, cmap_above, "Above Normal", 2 * spacing)
make_cb(ax, cmap_normal, "Normal", spacing)
make_cb(ax, cmap_below, "Below Normal", 0)

plt.tight_layout()

# --- Display and Download ---
st.pyplot(fig)

# Save figure to buffer for download
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Download button
st.download_button(
    label="Download Map as PNG",
    data=buf,
    file_name='rainfall_outlook_map.png',
    mime='image/png'
)
