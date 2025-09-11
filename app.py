import streamlit as st
import time

# setup
st.set_page_config(
    page_title="Regulatory Compliance Translator (RCT)",
    page_icon="assets/logo.jpg",
    layout="wide"
)

if "splash_done" not in st.session_state:
    st.session_state["splash_done"] = False

# if not st.session_state["splash_done"]:
#     st.image("assets/welcome_page.png",use_column_width=True)
#     time.sleep(2)
#     st.session_state["splash_done"] = True
#     st.rerun()
st.switch_page("pages/1_Upload.py")
