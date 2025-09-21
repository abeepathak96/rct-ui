import streamlit as st
import pandas as pd
from services import api_client

# ---- Page Config ----
st.set_page_config(page_title="RCT - Help & FAQs", layout="wide")
st.markdown("<h1 style='margin-bottom: 20px;'>ℹ️ Help & FAQs</h1>", unsafe_allow_html=True)

# ---- Collapsible FAQ Section ----
st.markdown("### ❓ Frequently Asked Questions")
with st.expander("What is this application about?"):
    st.markdown("This tool helps extract compliance requirements from regulatory documents using NLP.")

with st.expander("How do I upload a document?"):
    st.markdown(
        "Go to the 'Upload Documents' page and choose your file (PDF, DOCX, etc.). Then click 'Upload Document'.")

with st.expander("Why don't I see extracted requirements?"):
    st.markdown(
        "You must first run the extraction from the 'Extract Requirements' page. Once completed, results will appear there.")

with st.expander("Where are files stored?"):
    st.markdown("Files are securely stored in the backend server and not shared externally.")

st.divider()

# ---- Audit Logs Section ----
st.markdown("### 📜 Audit Logs")

logs = api_client.get_audit_logs()

if logs:
    df = pd.DataFrame(logs)

    # Format timestamp if exists
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    # Optional: rename columns for readability
    df.rename(columns={
        "timestamp": "Timestamp",
        "user": "User",
        "action": "Action",
        "details": "Details"
    }, inplace=True)

    # Apply simple styling
    styled_df = df.style.set_properties(**{
        'text-align': 'left',
        'padding': '8px 10px'
    }).set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('text-align', 'left')]},
        {'selector': 'td', 'props': [('border-color', '#ddd')]}
    ])

    st.dataframe(styled_df, use_container_width=True)
else:
    st.info("There are no audit logs available at the moment.")
