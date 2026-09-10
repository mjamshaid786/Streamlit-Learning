import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar Navigation Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Settings"],
        icons=["house", "book", "gear"], # Bootstrap icons
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("Home Page")
elif selected == "Projects":
    st.title("Projects Page")