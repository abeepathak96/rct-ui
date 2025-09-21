import streamlit as st
import pandas as pd
from services import api_client

st.set_page_config(page_title="RCT - Extract Requirements", layout="wide")
st.title("📑 Extract Requirements")

docs = api_client.get_documents()

if not docs:
    st.warning("⚠️ No documents available. Please upload one first.")
    st.stop()

selected_doc = st.selectbox(
    "Select a document:",
    options=[doc["doc_id"] for doc in docs],
    format_func=lambda x: f"{next(doc['doc_name'] for doc in docs if doc['doc_id']==x)}"
)

if st.button("Run NER Extraction"):
    with st.spinner("Extracting requirements..."):
        resp = api_client.extract_requirements(selected_doc)

    if resp.get("success"):
        st.success("✅ Extraction complete")
    else:
        st.error(f"❌ {resp.get('error')}")

st.divider()

# --- Fix: Get the list from the 'requirements' key ---
response = api_client.get_requirements(selected_doc)
requirements = response.get("requirements", [])

if requirements:
    st.subheader("📋 Extracted Requirements")
    st.dataframe(pd.DataFrame(requirements), use_container_width=True)
else:
    st.info("No requirements extracted yet.")
