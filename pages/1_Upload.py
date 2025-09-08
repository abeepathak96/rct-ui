import streamlit as st
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
# Using a wide layout for the main content area
st.set_page_config(
    page_title="Regulatory Compliance Translator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS STYLING ---
# Injecting custom CSS to match the mockup's design
st.markdown("""
<style>
    /* Hide Streamlit's default elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Main app background color */
    .main .block-container {
        background-color: #F8F9FA;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1E293B;
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] h2 {
        color: #FFFFFF;
        font-weight: 600;
    }
    [data-testid="stSidebar"] .st-emotion-cache-16txtl3 { /* Sidebar link container */
        gap: 0.5rem;
    }
    [data-testid="stSidebar"] a { /* Sidebar links */
        color: #CBD5E1;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        text-decoration: none;
    }
    /* Style for the active page link */
    [data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #334155;
        color: #FFFFFF;
        font-weight: 600;
    }

    /* File Uploader custom styling */
    [data-testid="stFileUploader"] {
        border: 2px dashed #D1D5DB;
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    [data-testid="stFileUploader"] label {
        font-weight: 600;
        color: #4B5563;
    }
    [data-testid="stFileUploader"] svg {
        color: #9CA3AF;
    }

    /* Custom styling for the list of recent uploads */
    .file-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 1.25rem;
        background-color: #FFFFFF;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid #E5E7EB;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .file-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .file-name {
        font-weight: 500;
        color: #1F2937;
    }
    .file-date {
        font-size: 0.8rem;
        color: #6B7280;
    }
    .file-icon {
        font-size: 1.5rem;
        color: #6B7280;
    }
    .menu-icon {
        cursor: pointer;
        color: #9CA3AF;
        font-weight: bold;
    }

    /* Center the "Start Analysis" button */
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    /* Style the "Start Analysis" button */
    .button-container .stButton>button {
        background-color: #111827;
        color: #FFFFFF;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        font-size: 1rem;
    }
    .button-container .stButton>button:hover {
        background-color: #374151;
        color: #FFFFFF;
    }

    /* Custom footer styling */
    .custom-footer {
        text-align: center;
        font-size: 0.8rem;
        color: #6B7280;
        padding: 1rem 0;
        border-top: 1px solid #E5E7EB;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("RCT")
    st.text_input("🔍 Search...", placeholder="Search...")
    st.markdown("---")

    # Using st.page_link for navigation links
    st.page_link("app.py", label="**Upload Documents**", icon="📄")
    st.page_link("app.py", label="Compliance Mapping", icon="🗺️")
    st.page_link("app.py", label="System Design", icon="⚙️")
    st.page_link("app.py", label="Reports & Downloads", icon="📊")
    st.page_link("app.py", label="Help/FAQ", icon="❓")

    # Spacer to push items to the bottom
    st.markdown("<div style='flex: 1;'></div>", unsafe_allow_html=True)

    st.toggle("Light/Dark Mode", key="dark_mode")

    st.markdown("---")
    st.caption("© 2025 Regulatory Compliance Translator (RCT)\nDeveloped for the AI Compliance Hackathon")


# --- MAIN CONTENT ---

# Page Header
st.header("Upload Compliance Documents")
st.write("Upload regulatory documents to extract compliance requirements")

# File Uploader
st.file_uploader(
    "Drag and drop your files here",
    type=['pdf', 'docx', 'csv', 'txt'],
    accept_multiple_files=True,
    label_visibility="collapsed"
)

# Buttons below the uploader
col1, col2, _ = st.columns([0.2, 0.2, 0.6])
with col1:
    st.button("Browse Files", use_container_width=True)
with col2:
    st.button("Paste Text", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Recent Uploads Section
st.subheader("Recent Uploads")

# Helper function to create a stylized file row
def file_row(icon, name, date):
    """Creates a stylized row for displaying a file."""
    st.markdown(f"""
    <div class="file-row">
        <div class="file-info">
            <span class="file-icon">{icon}</span>
            <div>
                <div class="file-name">{name}</div>
                <div class="file-date">Uploaded on {date}</div>
            </div>
        </div>
        <div class="menu-icon">⋮</div>
    </div>
    """, unsafe_allow_html=True)

# Mock data for recent files with dynamic dates
today = datetime.now()
file_row("📄", "GDPR_Compliance_2025.pdf", (today - timedelta(days=14)).strftime('%b %d, %Y'))
file_row("📄", "ISO27001_Requirements.docx", (today - timedelta(days=17)).strftime('%b %d, %Y'))
file_row("📄", "Compliance_Controls.csv", (today - timedelta(days=21)).strftime('%b %d, %Y'))

# Start Analysis Button
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("▶ Start Analysis"):
    with st.spinner('Analyzing documents...'):
        # Placeholder for analysis logic
        import time
        time.sleep(3)
    st.success("Analysis complete!")
st.markdown('</div>', unsafe_allow_html=True)


# --- FOOTER ---
st.markdown(
    """
    <div class="custom-footer">
        Team: ComplianceAI Solutions | Disclaimer: This tool provides suggestions only. Always consult with legal experts.
    </div>
    """,
    unsafe_allow_html=True
)
