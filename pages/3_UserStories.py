import streamlit as st
from services import api_client

st.set_page_config(page_title="RCT - User Stories", layout="wide")
st.title("📝 User Stories & Acceptance Criteria")

# ---- Fetch documents ----
docs = api_client.get_documents()
if not docs:
    st.warning("⚠️ No documents available. Please upload one first.")
    st.stop()

selected_doc = st.selectbox(
    "Select a document:",
    options=[doc["doc_id"] for doc in docs],
    format_func=lambda x: f"{next(doc['doc_name'] for doc in docs if doc['doc_id']==x)}"
)

# ---- Generate Button ----
if st.button("Generate User Stories"):
    with st.spinner("Generating user stories..."):
        resp = api_client.generate_userstories(selected_doc)
    if resp.get("success"):
        count = resp.get("count", 0)
        st.success(f"✅ {count} user stories generated successfully")
    else:
        st.error(f"❌ Failed: {resp.get('error', 'Unknown error')}")

st.divider()

# ---- Display Stories ----
stories = api_client.get_userstories(selected_doc)

if stories:
    st.subheader("Generated User Stories & Acceptance Criteria")

    for s in stories:
        with st.container():
            st.markdown(f"**📌 User Story {s['story_id']}**")
            st.markdown(f"**Requirement ID:** {s['requirement_id']}")
            st.markdown(f"**User Story:** {s['user_story_text']}")

            st.markdown("**Acceptance Criteria:**")
            if isinstance(s["acceptance_criteria"], list):
                for ac in s["acceptance_criteria"]:
                    st.markdown(f"- {ac}")
            else:
                st.markdown(f"- {s['acceptance_criteria']}")

            st.markdown("---")  # separator
else:
    st.info("No user stories available yet.")
