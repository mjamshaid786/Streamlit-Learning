import streamlit as st
import folium
from streamlit_folium import st_folium

# Lahore, Pakistan coordinates
m = folium.Map(location=[31.5204, 74.3587], zoom_start=12)
folium.Marker([31.5204, 74.3587], popup="Lahore", tooltip="Click for info").add_to(m)

st.title("Interactive Map")
st_data = st_folium(m, width=700, height=400)