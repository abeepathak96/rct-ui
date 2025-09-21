import streamlit as st
import pandas as pd
from services import api_client

st.set_page_config(page_title="RCT - Upload Documents", layout="wide")
st.title("📂 Upload Compliance Documents")

# ---- File Upload ----
uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "csv", "txt"])

if uploaded_file is not None:
    if st.button("Upload Document"):
        with st.spinner("Uploading..."):
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
    df = pd.DataFrame(docs)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No documents uploaded yet.")
