import streamlit as st
import pandas as pd
import time
from services import api_client

# ---- Page Config ----
st.set_page_config(page_title="RCT - Extract Requirements", layout="wide")
st.markdown("<h1 style='margin-bottom: 20px;'>📑 Extract Requirements</h1>", unsafe_allow_html=True)

# ---- Get Documents ----
docs = api_client.get_documents()

if not docs:
    st.warning("⚠️ No documents available. Please upload one first.")
    st.stop()

# ---- Document Selection ----
st.markdown("### 📄 Select Document")

selected_doc = st.selectbox(
    label="Choose a document to extract requirements from:",
    options=[doc["doc_id"] for doc in docs],
    format_func=lambda x: f"{next(doc['doc_name'] for doc in docs if doc['doc_id'] == x)}",
    help="Only documents that have been uploaded are listed here."
)

doc_name = next(doc['doc_name'] for doc in docs if doc['doc_id'] == selected_doc)

st.divider()

# ---- Extraction Trigger ----
st.markdown("### 🧠 Run NER Extraction")

if st.button("▶️ Run NER Extraction"):
    resp = api_client.extract_requirements(selected_doc)

    if resp.get("success"):
        st.info("✅ Extraction started. Checking progress...")

        progress_bar = st.progress(0)
        status_text = st.empty()

        while True:
            progress = api_client.get_extraction_progress(selected_doc)

            if progress["status"] == "completed":
                progress_bar.empty()
                status_text.empty()
                st.success("✅ Extraction completed!")
                break

            elif progress["status"] == "in_progress":
                progress_percent = progress.get("progress", 0)
                progress_bar.progress(progress_percent)
                status_text.info(f"🔄 Processing... {progress_percent}%")

            elif progress["status"] == "not_started":
                status_text.info("⏳ Waiting for extraction to start...")

            else:
                progress_bar.empty()
                status_text.error("⚠️ Error during extraction. Please try again.")
                break

            time.sleep(2)
    else:
        st.error(f"❌ Extraction failed: {resp.get('error', 'Unknown error')}")

st.divider()

# ---- Display Requirements ----
st.markdown(f"### 📋 Extracted Requirements for **{doc_name}**")

requirements = api_client.get_requirements(selected_doc)

if requirements:
    df = pd.DataFrame(requirements)

    # Format 'created_at' column (if present)
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M')

    # Styled DataFrame
    styled_df = df.style.set_properties(**{
        'text-align': 'left',
        'border-color': '#ddd',
        'border-width': '1px',
        'border-style': 'solid'
    })

    st.dataframe(styled_df, use_container_width=True)

    # ---- Download CSV Button ----
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download as CSV",
        data=csv,
        file_name="extracted_requirements.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    # Show warning and empty DataFrame with expected columns
    st.warning(f"⚠️ No requirements were found in the document **{doc_name}**.")

    empty_df = pd.DataFrame(columns=["requirement_id", "section_ref", "text", "category", "priority", "created_at"])
    st.dataframe(empty_df, use_container_width=True)
