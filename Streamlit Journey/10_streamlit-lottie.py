import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Page Layout Configuration
st.set_page_config(page_title="Lottie Animations Showcase", layout="wide")

# Helper function to load animation via URL with headers
def load_lottieurl(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None

# --- 1. Animation URLs Load Karein ---
# (Tested working CDN Lottie URLs)
anim_welcome = load_lottieurl("https://lottie.host/802b1f48-a006-444a-89a1-8bfbfa0d2358/a3kI1O5wP1.json")
anim_rocket  = load_lottieurl("https://lottie.host/625290b0-a548-4e8a-8670-36b132800538/7oP3U8CscJ.json")
anim_success = load_lottieurl("https://lottie.host/5b22bbf5-5e60-4c6e-90e9-b5478479e377/x2GZ47vK3x.json")
anim_coding  = load_lottieurl("https://lottie.host/2e23dbfb-2321-482a-9286-9a2c3fb64a32/qVnQv0Y5yM.json")
anim_analytics = load_lottieurl("https://lottie.host/2bc511ed-b5b8-4c81-b5bf-74e1dca4ff5b/f3M1bI4L1Z.json")

# --- SECTION 1: Hero Banner ---
st.title("🎬 Multi-Lottie Animation Playground")

col_head1, col_head2 = st.columns([2, 1])
with col_head1:
    st.subheader("Welcome to Streamlit Dashboard!")
    st.write("Is app mein hum aik saath multiple interactive aur vector Lottie animations test kar rahe hain.")

with col_head2:
    if anim_welcome:
        st_lottie(anim_welcome, height=180, key="welcome_hero")

st.divider()

# --- SECTION 2: 3-Column Features Showcase ---
st.subheader("⚡ Core Features Showcase")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💻 Web Development")
    if anim_coding:
        st_lottie(anim_coding, height=150, key="coding_card")
    st.info("Clean and responsive code structure.")

with col2:
    st.markdown("### 📊 Data Analytics")
    if anim_analytics:
        st_lottie(anim_analytics, height=150, key="analytics_card")
    st.info("Real-time data visualization.")

with col3:
    st.markdown("### 🚀 Fast Deployment")
    if anim_rocket:
        st_lottie(anim_rocket, height=150, speed=1.5, key="rocket_card")
    st.info("One-click cloud setup.")

st.divider()

# --- SECTION 3: Interactive Trigger & Form ---
col_form, col_action = st.columns(2)

with col_form:
    st.subheader("📝 User Feedback Form")
    with st.form("user_form"):
        name = st.text_input("Apna Naam Likhein")
        feedback = st.text_area("Feedback")
        submitted = st.form_submit_button("Submit Form")
        
        if submitted:
            if anim_success:
                st_lottie(anim_success, height=120, loop=False, key="success_form")
            st.success(f"Shukriya {name}! Aapka feedback submit ho gaya hai.")

with col_action:
    st.subheader("🎯 Custom Animation Controls")
    speed_val = st.slider("Animation Speed Adjust Karein:", 0.5, 3.0, 1.0, 0.5)
    
    if anim_rocket:
        st_lottie(
            anim_rocket,
            height=200,
            speed=speed_val,
            loop=True,
            key="interactive_rocket"
        )