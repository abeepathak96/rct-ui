import streamlit as st
import pandas as pd
from services import api_client
import time

st.set_page_config(page_title="RCT - Upload Documents", layout="wide")

# Custom CSS for better look and feel
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stFileUploader {
            background-color: #eaf2f8;
            padding: 20px;
            border-radius: 10px;
            border: 2px dashed #aaa;
        }
        .stTitle {
            color: #2c3e50;
            font-size: 32px;
        }
        .stSubheader {
            font-size: 20px;
            color: #2c3e50;
        }
        .stDataFrame {
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        .stText {
            font-size: 16px;
            color: #34495e;
        }
        .stProgress {
            height: 5px;
        }
        @media screen and (max-width: 768px) {
            .stTitle {
                font-size: 24px;
            }
            .stButton>button {
                width: 100%;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.title("📂 Upload Compliance Documents")

# ---- File Upload ----
uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "csv", "txt"])

if uploaded_file is not None:
    if st.button("Upload Document"):
        with st.spinner("Uploading..."):
            progress_bar = st.progress(0)
            for i in range(1, 101):
                progress_bar.progress(i)
                time.sleep(0.05)
            response = api_client.upload_document(uploaded_file)

        # backend returns {"Message": "..."}
        if "Message" in response:
            st.success(f"✅ {response['Message']}")
        else:
            st.error(f"❌ Upload failed: {response}")

st.divider()

# ---- List Documents ----
st.subheader("Uploaded Documents")

docs = api_client.get_documents()

if docs:
    # Sort by upload date (latest first)
    docs_sorted = sorted(docs, key=lambda x: x['upload_date'], reverse=True)

    for doc in docs_sorted:
        # Optional: format date nicely
        upload_date = doc['upload_date'].split('T')[0]  # keep just the date part

        # Render each document as a card
        st.markdown(f"""
            <div style="
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 15px;
                background-color: #f9f9f9;
            ">
                <h5 style="margin-bottom: 10px;">📄 {doc['doc_name']}</h5>
                <p><strong>Type:</strong> {doc['doc_type']}</p>
                <p><strong>Status:</strong> {doc['status'].capitalize()}</p>
                <p><strong>Uploaded on:</strong> {upload_date}</p>
            </div>
        """, unsafe_allow_html=True)

else:
    st.info("No documents uploaded yet.")


