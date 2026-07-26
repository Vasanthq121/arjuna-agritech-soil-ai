if page == "Dashboard":

    st.header("Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Reports", 0)

    c2.metric("Chats", 0)

    c3.metric("Analyses", 0)

    st.info("Upload your first soil report.")