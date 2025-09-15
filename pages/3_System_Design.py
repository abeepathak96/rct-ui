# pages/5_System_Design.py
import streamlit as st

st.set_page_config(page_title="System Design", layout="wide")

st.title("System Design")
st.caption("Visualize system modules and their compliance requirements")

# --- Mock modules data ---
modules = {
    "Data Ingestion": {
        "status": "Finalized",
        "requirements": 4,
        "description": "Handle the intake of regulatory data from multiple sources and formats for processing.",
        "linked_reqs": ["REQ-004: Data Processing Security", "REQ-008: Regulatory Update Handling"]
    },
    "Processing Engine": {
        "status": "In Review",
        "requirements": 6,
        "description": "Core system component that transforms regulatory text into structured compliance requirements using NLP/LLMs.",
        "linked_reqs": ["REQ-012: Processing Accuracy", "REQ-016: Data Transformation Standards", "REQ-023: Compliance Mapping"]
    },
    "UI/UX": {
        "status": "Finalized",
        "requirements": 3,
        "description": "User interface components and workflows designed for regulatory compliance review.",
        "linked_reqs": ["REQ-031: Performance Metrics"]
    },
    "APIs & Interfaces": {
        "status": "Draft",
        "requirements": 5,
        "description": "Integration points with external systems and data exchange protocols.",
        "linked_reqs": []
    },
    "Audit & Logging": {
        "status": "Finalized",
        "requirements": 2,
        "description": "Comprehensive logging of system activities and user interactions for compliance verification.",
        "linked_reqs": []
    },
    "Compliance Rules Engine": {
        "status": "In Review",
        "requirements": 8,
        "description": "Logic framework for interpreting and applying regulatory rules to system contexts.",
        "linked_reqs": []
    }
}

# --- Layout ---
left, right = st.columns([2, 3])

with left:
    st.subheader("Modules")
    for module, details in modules.items():
        st.button(
            f"{module} ({details['requirements']} reqs, {details['status']})",
            key=module
        )

with right:
    st.subheader("Processing Engine")
    st.caption("Status: In Review | Last updated: Aug 25, 2025")

    st.markdown("**Description**")
    st.info(modules["Processing Engine"]["description"])

    st.markdown("**Linked Compliance Requirements**")
    for req in modules["Processing Engine"]["linked_reqs"]:
        st.write(f"- {req}")

# --- Footer Actions ---
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.button("➕ Add New Module")
with col2:
    st.button("💾 Save Design")
with col3:
    st.button("📄 Generate System Architecture Report", use_container_width=True)

# --- Progress ---
st.progress(4 / 6)
st.caption("Progress: 4 of 6 Modules Completed")
