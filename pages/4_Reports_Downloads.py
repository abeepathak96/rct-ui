# pages/6_Reports_Downloads.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reports & Downloads", layout="wide")

st.title("Reports & Downloads")
st.caption("Access, review, and download compliance reports")

# --- Filters ---
col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
with col1:
    framework = st.selectbox("Framework", ["All Frameworks", "Basel III", "GDPR", "PSD2", "SOX"])
with col2:
    date_range = st.selectbox("Date Range", ["All Time", "Last 7 Days", "Last 30 Days", "This Year"])
with col3:
    reviewer = st.selectbox("Reviewer", ["All Reviewers", "John Doe", "Jane Smith", "Alex Johnson"])
with col4:
    search = st.text_input("Search documents")

st.write("---")

# --- Mock data for reports ---
data = [
    ["2025-09-27", "Basel III Capital Requirements Analysis", "Basel III", "Completed", "John Doe"],
    ["2025-09-25", "GDPR Compliance Assessment", "GDPR", "Completed", "Jane Smith"],
    ["2025-09-20", "PSD2 Strong Customer Authentication Analysis", "PSD2", "In Progress", "Alex Johnson"],
    ["2025-09-18", "Basel III Liquidity Coverage Ratio Assessment", "Basel III", "Needs Review", "John Doe"],
]

df = pd.DataFrame(data, columns=["Date", "Document Name", "Framework", "Status", "Reviewer"])

# --- Layout with table and preview ---
left, right = st.columns([3, 2])

with left:
    st.subheader("Available Reports")
    st.dataframe(df, use_container_width=True)

    # Pagination placeholder
    st.caption("Showing 1 to 4 of 12 results")
    st.button("⬅️ Previous")
    st.button("Next ➡️")

with right:
    st.subheader("Report Preview")
    st.caption("Basel III Capital Requirements Analysis — Generated on Aug 27, 2025")

    st.metric("Total Clauses", 143)
    st.metric("Reviewed", "120 (84%)")
    st.metric("Pending", "23 (16%)")
    st.metric("Reviewer", "John Doe")

    st.markdown("**Summary**")
    st.write(
        "- Data encryption measures confirmed\n"
        "- Audit logging controls in place\n"
        "- Gaps in reporting automation\n"
        "- Compliance risk reduced by 30%\n"
    )

    st.markdown("**Download Options**")
    st.button("📄 Open Full Report")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("⬇️ PDF")
    with col2:
        st.button("⬇️ DOCX")
    with col3:
        st.button("⬇️ CSV")

st.write("---")

# --- Footer Actions ---
col1, col2 = st.columns([1, 2])
with col1:
    st.button("📤 Upload New Document for Analysis")
with col2:
    st.button("📊 Generate Consolidated Report", use_container_width=True)
