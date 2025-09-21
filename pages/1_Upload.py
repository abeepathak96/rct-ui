import streamlit as st
import pandas as pd
from services import api_client

# Set page config and title
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

# Title of the page
st.title("📂 Upload Compliance Documents")

# ---- File Upload ----
uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "csv", "txt"], help="Only .pdf, .docx, .csv, and .txt files are allowed.")

if uploaded_file is not None:
    if st.button("Upload Document", help="Upload your document", icon="upload"):
        with st.spinner("Uploading..."):
            # Optional: Progress bar for better UX during upload
            progress_bar = st.progress(0)
            for i in range(1, 101):
                progress_bar.progress(i)
                time.sleep(0.05)  # Simulate upload delay (remove in production)

            # Call backend API to upload the document
            response = api_client.upload_document(uploaded_file)

        if "Message" in response:
            st.success(f"✅ {response['Message']}")
        else:
            st.error(f"❌ Upload failed: {response}")

st.divider()

# ---- List Documents ----
st.subheader("Uploaded Documents")

# Fetch the list of uploaded documents
docs = api_client.get_documents()

if docs:
    # Sort the documents by upload date (assuming `upload_date` is available)
    docs_sorted = sorted(docs, key=lambda x: x['upload_date'], reverse=True)

    # Display each document in a visually appealing card layout
    for doc in docs_sorted:
        st.markdown(f"""
            <div style="border: 2px solid #ddd; border-radius: 10px; padding: 15px; margin-bottom: 15px; background-color: #f9f9f9;">
                <h5>{doc['name']}</h5>
                <p><strong>Type:</strong> {doc['type']}</p>
                <p><strong>Uploaded on:</strong> {doc['upload_date']}</p>
                <a href="{doc['download_url']}" target="_blank">
                    <button style="background-color: #3498db; color: white; border: none; padding: 8px 16px; border-radius: 5px;">Download</button>
                </a>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("No documents uploaded yet.")
