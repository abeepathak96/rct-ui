import streamlit as st

st.set_page_config(page_title="Help & FAQ", layout="wide")

st.title("Help & FAQ")
st.caption("Find answers to common questions and access resources")

# --- Search bar ---
st.text_input("🔍 How can we help you today?", placeholder="Search FAQs, Guides, or Keywords")

st.write("---")

# --- Two-column layout ---
left, right = st.columns([2, 1])

with left:
    st.subheader("Frequently Asked Questions")

    with st.expander("General Usage"):
        st.write("**What is the Regulatory Compliance Translator?**")
        st.caption("A tool designed to help organizations understand and map regulatory requirements into structured system artifacts.")
        st.write("**How do I navigate the dashboard?**")
        st.caption("Use the left sidebar to access Upload, Mapping, System Design, and Reports pages.")

    with st.expander("Uploading Documents"):
        st.write("**What file formats are supported?**")
        st.caption("PDF, DOCX, CSV, TXT are supported for upload.")
        st.write("**Is there a file size limit?**")
        st.caption("Yes, each file should be under 200MB.")

    with st.expander("Compliance Mapping"):
        st.write("**How does the mapping algorithm work?**")
        st.caption("It uses AI/LLMs to extract obligations and map them to requirements with traceability.")

    with st.expander("System Design"):
        st.write("**Can I create custom modules?**")
        st.caption("Yes, use the 'Add New Module' option on the System Design page.")

    with st.expander("Reports & Downloads"):
        st.write("**What report formats are available?**")
        st.caption("You can export reports as PDF, DOCX, or CSV.")

with right:
    st.subheader("Quick Links")
    st.button("📘 User Guide (PDF)")
    st.button("🎥 Video Tutorial")
    st.button("⚙️ API Documentation")
    st.button("📖 Glossary of Terms")

    st.subheader("Need More Help?")
    st.caption("Available Monday–Friday, 9 AM – 6 PM")
    st.write("📞 +1 (555) 123-4567")
    st.write("📧 support@complianceai.com")

st.write("---")

# --- Contact Support Form ---
st.subheader("Contact Support")
with st.form("support_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Your Query", height=120)
    submitted = st.form_submit_button("Submit Query")
    if submitted:
        st.success("✅ Your query has been submitted. Support will respond within 24 hours.")