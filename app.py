# app.py
import streamlit as st
import base64
from pathlib import Path

# --- Helper Function ---
def get_image_as_base64(path: str) -> str:
    """
    Reads an image file from the given path and returns it
    as a Base64 encoded string.
    """
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image file not found at {path}. Please check the file path.")
        return ""

# --- Configuration ---
LOGO_PATH = "assets/logo.jpg"
WELCOME_IMAGE_PATH = "assets/welcome_page.png"

# --- Page Setup ---
st.set_page_config(
    page_title="Regulatory Compliance Translator (RCT)",
    page_icon=LOGO_PATH if Path(LOGO_PATH).exists() else "🤖",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# --- Clickable Welcome Page ---

# Encode the local image to a Base64 string for robust embedding
welcome_image_base64 = get_image_as_base64(WELCOME_IMAGE_PATH)

if welcome_image_base64:
    # This HTML/CSS block creates a fullscreen, clickable image.
    # Clicking the image adds '?page=upload' to the URL.
    st.markdown(
        f"""
        <style>
            /* Remove Streamlit's default padding */
            .main .block-container {{
                padding: 0;
                margin: 0;
            }}
            /* Style for the fullscreen container */
            .full-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                width: 100vw;
                position: fixed;
                top: 0;
                left: 0;
                background-color: white; /* Optional: background for the splash */
            }}
            .full-container img {{
                max-width: 95%;
                max-height: 95%;
                object-fit: contain;
                cursor: pointer;
            }}
        </style>
        <a href="?page=upload" target="_self">
            <div class="full-container">
                <img src="data:image/png;base64,{welcome_image_base64}" alt="Welcome Page">
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# --- Navigation Logic ---
# This checks the URL's query parameters. If 'page=upload' is present,
# it switches to the Upload page.
if st.query_params.get("page") == ["upload"]:
    st.switch_page("pages/1_Upload.py")