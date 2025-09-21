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
    if st.button("Upload Document",icon="upload"):
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
st.write(type(docs))
st.write(docs)
if docs:
    df = pd.DataFrame(docs)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No documents uploaded yet.")
