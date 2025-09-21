import streamlit as st
import pandas as pd
from services import api_client

st.set_page_config(page_title="RCT - User Stories", layout="wide")
st.title("📝 User Stories & Acceptance Criteria")

docs = api_client.get_documents()
if not docs:
    st.warning("⚠️ No documents available. Please upload one first.")
    st.stop()

selected_doc = st.selectbox(
    "Select a document:",
    options=[doc["doc_id"] for doc in docs],
    format_func=lambda x: f"{next(doc['doc_name'] for doc in docs if doc['doc_id']==x)}"
)

if st.button("Generate User Stories"):
    with st.spinner("Generating user stories..."):
        resp = api_client.generate_userstories(selected_doc)
    if resp.get("success"):
        st.success("✅ User stories generated successfully")
    else:
        st.error(f"❌ {resp.get('error')}")

st.divider()
stories = api_client.get_userstories(selected_doc)
if stories:
    st.subheader("Generated User Stories & Acceptance Criteria")
    st.dataframe(pd.DataFrame(stories), use_container_width=True)
else:
    st.info("No user stories available yet.")
