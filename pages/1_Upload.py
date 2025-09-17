import streamlit as st
import requests
import os
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Regulatory Compliance Translator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- BACKEND CONFIG ---
API_BASE_URL = os.getenv("API_BASE_URL", "https://rct-backend-908a.onrender.com")  # change to Render URL when deployed

# --- Page Header ---
st.title("Upload Compliance Document")
st.caption("Upload regulatory documents to extract compliance requirements")

# --- Upload Box ---
uploaded_file = st.file_uploader(
    "Drag and drop your files here (PDF,DOCX,CSV,TXT)",
    type=["pdf", "docx", "csv", "txt"]
)

if uploaded_file:
    if st.button("📤 Upload to Server"):
        try:
            with st.spinner("Uploading file..."):
                response = requests.post(
                    f"{API_BASE_URL}/rct/documents/upload",
                    files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                )
                if response.status_code == 200:
                    st.success(f"✅ File uploaded successfully!")
                    st.json(response.json())  # Show API response
                else:
                    st.error(f"❌ Upload failed: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Error uploading file: {e}")

st.write("---")

# --- Recent Uploads ---
st.subheader("Recent Uploads")

try:
    response = requests.get(f"{API_BASE_URL}/rct/documents")
    if response.status_code == 200:
        documents = response.json().get("files", [])
        for doc in documents:
            st.write(f"📄 {doc['name']} — Uploaded on {doc['upload_ts']}")
    else:
        st.warning("Could not fetch recent uploads from API.")
except Exception as e:
    st.warning(f"⚠️ API not reachable: {e}")

st.write("---")

# --- Start Analysis Button ---
st.button("▶️ Start Analysis", use_container_width=True)

# --- Footer ---
st.caption(
    "© 2025 Regulatory Compliance Translator (RCT) | Developed for the AI Compliance Hackathon\n\n"
    "Disclaimer: This tool provides suggestions only. Always consult with legal experts."
)