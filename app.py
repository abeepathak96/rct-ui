import streamlit as st

# setup
st.set_page_config(
    page_title="Regulatory Compliance Translator (RCT)",
    page_icon="assets/logo.jpg",
    layout="centered"
)

# Centered Layout
st.markdown(
 """
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        margin-top: 20px;
    }
    .subtitle {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        max-width: 600px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown('<div class="centered">',unsafe_allow_html=True)

st.image("assets/logo.jpg",width=180)

st.markdown('<div class="title">Regulatory Compliance Translator (RCT)</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Transform regulatory documents into actionable '
    'engineering artifacts (user stories & acceptance criteria) with full '
    'traceability for compliance teams.</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
