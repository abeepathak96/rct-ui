import streamlit as st
import pandas as pd
from services import api_client

st.set_page_config(page_title="RCT - Help & FAQs", layout="wide")
st.title("ℹ️ Help & FAQs")

logs = api_client.get_audit_logs()

if logs:
    st.subheader("Audit Logs")
    st.dataframe(pd.DataFrame(logs), use_container_width=True)
else:
    st.info("No audit logs available.")
