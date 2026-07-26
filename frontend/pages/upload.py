import streamlit as st

st.title("📄 Upload Soil Report")

uploaded = st.file_uploader(
    "Choose a soil report",
    type=["pdf"]
)

crop = st.text_input("Crop")

if st.button("Analyze"):
    st.success("Ready to connect to FastAPI")