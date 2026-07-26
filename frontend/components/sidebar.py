with st.sidebar:

    st.title("🌱 Soil AI")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Upload Report",
            "AI Chat",
            "Reports"
        ]
    )