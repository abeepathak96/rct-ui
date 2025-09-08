import streamlit as st
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
# Set the page configuration for a wide layout.
st.set_page_config(
    page_title="Regulatory Compliance Translator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ACCURATE CSS STYLING ---
# This CSS is carefully crafted to match the mockup's design.
st.markdown("""
<style>
    /* --- General & Core App --- */
    /* Hide Streamlit's default elements for a custom look */
    #MainMenu, header, footer {
        visibility: hidden;
    }
    /* Set a light grey background for the main content area */
    .main .block-container {
        padding: 2rem 2rem 1rem 2rem;
        background-color: #F0F2F6; /* Light grey background */
    }

    /* --- Sidebar Styling --- */
    [data-testid="stSidebar"] {
        background-color: #0F172A; /* Dark Slate Blue */
        padding: 1.5rem;
    }
    [data-testid="stSidebar"] h2 {
        color: #FFFFFF;
        font-weight: 600;
        font-size: 1.5rem; /* Larger title */
        padding-bottom: 1rem;
    }
    [data-testid="stSidebar"] .stTextInput input {
        background-color: #1E293B;
        color: #E2E8F0;
    }
    [data-testid="stSidebar"] a { /* Navigation links */
        color: #94A3B8; /* Lighter text for inactive links */
        border-radius: 0.375rem;
        padding: 0.75rem 1rem;
        text-decoration: none;
        font-weight: 500;
        transition: background-color 0.2s, color 0.2s;
    }
    [data-testid="stSidebar"] a:hover {
        background-color: #1E293B;
        color: #FFFFFF;
    }
    /* Active page link style */
    [data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #334155;
        color: #FFFFFF;
        font-weight: 600;
    }
    [data-testid="stSidebar"] .st-emotion-cache-1aehpv { /* Divider line */
        background-color: #334155;
    }
    [data-testid="stSidebar"] .st-emotion-cache-1gulkj5 { /* Toggle switch container */
        margin-top: auto; /* Push to bottom */
    }
    [data-testid="stSidebar"] .stCaption {
        color: #64748B;
        padding-top: 1rem;
    }


    /* --- Main Content Styling --- */
    /* File Uploader custom styling */
    [data-testid="stFileUploader"] {
        border: 2px dashed #CBD5E1;
        background-color: #FFFFFF;
        padding: 2.5rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    [data-testid="stFileUploader"] svg { font-size: 3rem; }
    [data-testid="stFileUploader"] small { font-size: 1rem; color: #64748B; }

    /* Buttons below uploader */
    .stButton>button {
        border-radius: 0.5rem;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
    }
    .stButton>button[kind="secondary"] { /* Browse files button */
        background-color: #475569;
        color: #FFFFFF;
    }
    .stButton>button[kind="secondary"]:hover {
        background-color: #334155;
        color: #FFFFFF;
    }

    /* Recent Uploads List */
    .file-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 1.25rem;
        background-color: #FFFFFF;
        border-radius: 0.5rem;
        margin-bottom: 0.75rem;
        border: 1px solid #E2E8F0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .file-info { display: flex; align-items: center; gap: 0.75rem; }
    .file-icon { font-size: 1.5rem; color: #64748B; }
    .file-name { font-weight: 500; color: #1F2937; }
    .file-date { font-size: 0.85rem; color: #64748B; }
    .menu-icon { cursor: pointer; color: #94A3B8; font-weight: bold; font-size: 1.2rem; }

    /* Start Analysis Button */
    .center-button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    .center-button-container .stButton>button {
        background-color: #111827;
        color: #FFFFFF;
        font-size: 1rem;
        padding: 0.75rem 2.5rem;
        border-radius: 0.5rem;
    }
    .center-button-container .stButton>button:hover {
        background-color: #374151; color: #FFFFFF;
    }

    /* Custom Footer */
    .custom-footer {
        text-align: center;
        font-size: 0.85rem;
        color: #64748B;
        padding: 1.5rem 0;
        border-top: 1px solid #E2E8F0;
        margin-top: auto; /* Pushes footer to bottom */
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Regulatory Compliance Translator (RCT)")
    st.text_input("🔍 Search...", placeholder="Search...", label_visibility="collapsed")
    st.divider()

    # Navigation links
    st.page_link("app.py", label="**Upload Documents**", icon="📄")
    st.page_link("app.py", label="Compliance Mapping", icon="🗺️")
    st.page_link("app.py", label="System Design", icon="⚙️")
    st.page_link("app.py", label="Reports & Downloads", icon="📊")
    st.page_link("app.py", label="Help/FAQ", icon="❓")

    # Spacer to push bottom content down
    st.markdown("<div style='flex: 1;'></div>", unsafe_allow_html=True)

    st.toggle("Light/Dark Mode")
    st.caption("© 2025 Regulatory Compliance Translator (RCT) | Developed for the AI Compliance Hackathon")

# --- MAIN CONTENT ---

# Top Header Section (Title + Icons)
col1, col_spacer, col2, col3 = st.columns([6, 1, 0.5, 0.5])
with col1:
    st.title("Upload Compliance Documents")
    st.caption("Upload regulatory documents to extract compliance requirements")
with col2:
    st.button("🔔", help="Notifications", use_container_width=True)
with col3:
    st.button("👤", help="Profile", use_container_width=True)

st.divider()

# File Uploader
st.file_uploader(
    "Drag and drop your files here",
    type=['pdf', 'docx', 'csv', 'txt'],
    accept_multiple_files=True,
    label_visibility="collapsed"
)

# Buttons: "Browse Files" and "Paste Text"
btn_col1, btn_col2, _ = st.columns([0.2, 0.2, 0.6])
with btn_col1:
    st.button("📁 Browse Files", use_container_width=True)
with btn_col2:
    st.button("📋 Paste Text", use_container_width=True, type="secondary")

st.markdown("<br>", unsafe_allow_html=True)

# Recent Uploads Section
st.subheader("Recent Uploads")

# Helper function to render a custom file row using HTML
def file_row_display(icon, name, date):
    st.markdown(f"""
    <div class="file-row">
        <div class="file-info">
            <span class="file-icon">{icon}</span>
            <div>
                <div class="file-name">{name}</div>
                <div class="file-date">Uploaded on {date}</div>
            </div>
        </div>
        <span class="menu-icon">⋮</span>
    </div>
    """, unsafe_allow_html=True)

# Displaying mock recent files
today = datetime(2025, 8, 25) # Using a fixed date for consistency with mockup
file_row_display("📄", "GDPR_Compliance_2025.pdf", today.strftime('%b %d, %Y'))
file_row_display("📄", "ISO27001_Requirements.docx", (today - timedelta(days=3)).strftime('%b %d, %Y'))
file_row_display("📄", "Compliance_Controls.csv", (today - timedelta(days=7)).strftime('%b %d, %Y'))

# Start Analysis Button (Centered)
st.markdown('<div class="center-button-container">', unsafe_allow_html=True)
if st.button("▶ Start Analysis"):
    with st.spinner('Analyzing documents...'):
        import time
        time.sleep(2)
    st.success("Analysis complete!")
st.markdown('</div>', unsafe_allow_html=True)

# Custom Footer
st.markdown(
    """
    <div class="custom-footer">
        Team: ComplianceAI Solutions | Disclaimer: This tool provides suggestions only. Always consult with legal experts.
    </div>
    """,
    unsafe_allow_html=True
)

