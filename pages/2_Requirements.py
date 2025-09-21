import streamlit as st
import pandas as pd
import time
from services import api_client

st.set_page_config(page_title="RCT - Extract Requirements", layout="wide")
st.title("📑 Extract Requirements")

# ---- Get documents ----
docs = api_client.get_documents()
if not docs:
    st.warning("⚠️ No documents available. Please upload one first.")
    st.stop()

selected_doc = st.selectbox(
    "Select a document:",
    options=[doc["doc_id"] for doc in docs],
    format_func=lambda x: f"{next(doc['doc_name'] for doc in docs if doc['doc_id']==x)}"
)

# ---- Extraction Trigger ----
if st.button("Run NER Extraction"):
    resp = api_client.extract_requirements(selected_doc)
    if resp.get("success"):
        st.info("Extraction started. Checking progress...")

        progress_bar = st.progress(0)
        status_text = st.empty()

        while True:
            progress = api_client.get_extraction_progress(selected_doc)
            if progress["status"] == "completed":
                progress_bar.progress(100)
                status_text.text("✅ Extraction completed!")
                break
            elif progress["status"] == "in_progress":
                progress_bar.progress(progress["progress"])
                status_text.text(f"Processing... {progress['progress']}%")
            elif progress["status"] == "not_started":
                status_text.text("⏳ Waiting for extraction to start...")
            else:
                status_text.text("⚠️ Error during extraction.")
                break
            time.sleep(2)

# ---- Display Requirements ----
requirements = api_client.get_requirements(selected_doc)
if requirements:
    st.subheader("Extracted Requirements")
    st.dataframe(pd.DataFrame(requirements), use_container_width=True)
else:
    st.info("No requirements extracted yet.")
