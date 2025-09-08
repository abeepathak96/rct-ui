import streamlit as st
import datetime

st.set_page_config(
    page_title="Upload Documents",
    page_icon="assets/logo.jpg",
    layout="wide"
)

st.sidebar.title("Regulatory Compliance Translator (RCT)")
st.sidebar.caption("Map regulations to system requirements with AI")

menu_itmes = [
    "Upload Documents",
    "Compliance Mapping",
    "System Design",
    "Rports & Downloads",
    "Help/FAQ"
]

for item in menu_itmes:
    if item == "Upload Documents":
        st.sidebar.button(item, key=item, type="primary")
    else:
        st.sidebar.button(item, key=item)

st.title("Upload Compliance Documents")
st.caption("Upload regulatory documents to extract compliance requirements")

uploaded_file = st.file_uploader(
    "Drag and drop your files here",
    type=["pdf","docx","csv","txt"],
    label_visibility="collapsed"
)

col1,col2 = st.columns([1,1])
with col1:
    st.button("📂 Browse Files")
with col2:
    st.button("📝 Paste Text")

st.markdown("---")

st.subheader("Recent Uploads")
recent_uploads  = [
    {"name": "GDPR_Compliance_2025.pdf", "date": datetime.date(2025, 8, 25)},
    {"name": "ISO27001_Requirements.docx", "date": datetime.date(2025, 8, 22)},
    {"name": "Compliance_Controls.csv", "date": datetime.date(2025, 8, 18)}
]

for doc in recent_uploads:
    st.write(f"📄 {doc['name']}  —  Uploaded on {doc['date'].strftime('%b %d, %Y')}")

st.markdown("---")

st.button("▶️ Start Analysis", use_container_width=True, type="primary")

# --- Footer ---
st.markdown(
    """
    <div style="text-align:center; font-size: 0.85em; color: gray; margin-top: 30px;">
    © 2025 Regulatory Compliance Translator (RCT) | Developed for the AI Compliance Hackathon  
    <br>Disclaimer: This tool provides suggestions only. Always consult with legal experts.
    </div>
    """,
    unsafe_allow_html=True
)
