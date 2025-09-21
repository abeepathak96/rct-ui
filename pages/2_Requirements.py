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

requirements = api_client.get_requirements(selected_doc)

# Defensive check in case the backend ever changes
if not isinstance(requirements, list):
    st.error("❌ Invalid response from API. Expected a list of requirements.")
    st.stop()

if requirements:
    st.subheader("📋 Extracted Requirements")
    df = pd.DataFrame(requirements)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No requirements extracted yet.")
