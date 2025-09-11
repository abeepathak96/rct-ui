import streamlit as st
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
# Set the page configuration for a wide layout.
st.set_page_config(
    page_title="Regulatory Compliance Translator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Page Header ---#
st.title("Upload Compliance Document")
st.caption("Upload regulatory documents to extract compliance requirements")

#--- Upload Box ---#
uploaded_file = st.file_uploader(
    "Drag and drop your files here (PDF,DOCX,CSV,TXT)",
    type=["pdf","docx","csv","txt"]
)

col1,col2 = st.columns(2)
with col1:
    st.button("📂 Browse Files")
with col2:
    st.button("📝 Paste Text")

st.write("---")

# --- Recent Uploads (mock data for now) ---
st.subheader("Recent Uploads")
recent_uploads = [
    {"name": "GDPR_Compliance_2025.pdf", "date": "Aug 25, 2025"},
    {"name": "ISO27001_Requirements.docx", "date": "Aug 22, 2025"},
    {"name": "Compliance_Controls.csv", "date": "Aug 18, 2025"},
]

for doc in recent_uploads:
    st.write(f"📄 {doc['name']} — Uploaded on {doc['date']}")

st.write("---")

# --- Start Analysis Button ---
st.button("▶️ Start Analysis", use_container_width=True)

# --- Footer ---
st.caption(
    "© 2025 Regulatory Compliance Translator (RCT) | Developed for the AI Compliance Hackathon\n\n"
    "Disclaimer: This tool provides suggestions only. Always consult with legal experts."
)