import streamlit as st
import datetime

st.set_page_config(page_title="Upload Documents", layout="wide")

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    /* Upload box */
    .upload-box {
        border: 2px dashed #ccc;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        background-color: #f8f9fa;
        margin-bottom: 20px;
    }
    .upload-box:hover {
        border-color: #4A90E2;
        background-color: #f1faff;
    }

    /* Buttons */
    .stButton button {
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
    }
    .browse-btn {
        background-color: #4A90E2 !important;
        color: white !important;
    }
    .paste-btn {
        background-color: #6c757d !important;
        color: white !important;
    }
    .analyze-btn {
        width: 100%;
        background-color: #e74c3c !important;
        color: white !important;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.8rem;
        border-radius: 6px;
    }

    /* Recent uploads list */
    .file-list {
        margin-top: 15px;
    }
    .file-item {
        padding: 10px;
        border-bottom: 1px solid #ddd;
        font-size: 0.95rem;
    }
    .file-item:last-child {
        border-bottom: none;
    }
    .file-icon {
        margin-right: 8px;
        color: #4A90E2;
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 0.85em;
        color: gray;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Header ---
st.title("Upload Compliance Documents")
st.caption("Upload regulatory documents to extract compliance requirements")

# --- Upload Box (Styled) ---
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Drag and drop your files here",
    type=["pdf", "docx", "csv", "txt"],
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.button("📂 Browse Files", key="browse", type="secondary")
with col2:
    st.button("📝 Paste Text", key="paste", type="secondary")

st.markdown("---")

# --- Recent Uploads (Mock Data for now) ---
st.subheader("Recent Uploads")
recent_uploads = [
    {"name": "GDPR_Compliance_2025.pdf", "date": datetime.date(2025, 8, 25)},
    {"name": "ISO27001_Requirements.docx", "date": datetime.date(2025, 8, 22)},
    {"name": "Compliance_Controls.csv", "date": datetime.date(2025, 8, 18)}
]

st.markdown('<div class="file-list">', unsafe_allow_html=True)
for doc in recent_uploads:
    st.markdown(
        f'<div class="file-item">📄 <span class="file-icon"></span>'
        f'{doc["name"]} — Uploaded on {doc["date"].strftime("%b %d, %Y")}</div>',
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- Start Analysis Button ---
st.markdown('<div style="margin-top:20px;">', unsafe_allow_html=True)
st.button("▶️ Start Analysis", key="analyze", type="primary")
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <div class="footer">
    © 2025 Regulatory Compliance Translator (RCT) | Developed for the AI Compliance Hackathon  
    <br>Disclaimer: This tool provides suggestions only. Always consult with legal experts.
    </div>
    """,
    unsafe_allow_html=True
)