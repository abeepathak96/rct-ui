# app.py
import streamlit as st
import os

# Setup
st.set_page_config(
    page_title="Regulatory Compliance Translator (RCT)",
    page_icon="assets/logo.jpg",
    layout="wide",
    initial_sidebar_state="collapsed"   # 👈 collapse sidebar by default
)

# CSS for fullscreen image
st.markdown("""
    <style>
    .full-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;  /* full viewport height */
    }
    .full-container img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Image path
image_path = os.path.join(os.getcwd(), "assets", "welcome_page.png")

# Fullscreen splash with clickable image
st.markdown(
    f"""
    <div class="full-container">
        <a href="?page=upload">
            <img src="file://{image_path}" alt="Welcome Page">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Handle redirect when clicked
query_params = st.query_params
if query_params.get("page") == ["upload"]:
    st.switch_page("pages/1_Upload.py")
