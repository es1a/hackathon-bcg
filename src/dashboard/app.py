import streamlit as st


st.set_page_config(page_title="Farmer Advisory Dashboard", layout="wide")
st.title("Farmer Advisory & Early-Warning System")
st.info("Dashboard scaffold. Connect this view to the API dashboard endpoints next.")

col1, col2, col3 = st.columns(3)
col1.metric("Open incidents", "—")
col2.metric("Reports in last 3 days", "—")
col3.metric("Regional alerts", "—")

st.subheader("Incident map")
st.caption("Map, filters, evidence, and recommendation rationale will be added here.")

