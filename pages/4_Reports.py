import streamlit as st
from services import api_client

st.set_page_config(page_title="RCT - Reports", layout="wide")
st.title("📊 Reports")

docs = api_client.get_documents()
if not docs:
    st.warning("⚠️ No documents available.")
    st.stop()

selected_doc = st.selectbox(
    "Select a document to generate a report:",
    options=[doc["id"] for doc in docs],
    format_func=lambda x: f"{next(doc['name'] for doc in docs if doc['id']==x)}"
)

if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        resp = api_client.generate_report(selected_doc)
    if resp.get("success"):
        st.success(f"✅ Report generated: {resp['report_id']}")
    else:
        st.error(f"❌ {resp.get('error')}")

st.divider()
report_id = st.text_input("Enter Report ID to download:")

format_choice = st.selectbox("Select format:", ["pdf", "docx", "csv"])
if st.button("Download Report"):
    if report_id:
        file_bytes = api_client.download_report(report_id, format_choice)
        if file_bytes:
            st.download_button(
                label=f"Download {format_choice.upper()}",
                data=file_bytes,
                file_name=f"report_{report_id}.{format_choice}",
                mime="application/octet-stream"
            )
        else:
            st.error("❌ Failed to download report.")
    else:
        st.warning("Enter a report ID first.")
