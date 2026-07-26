import os
import tempfile
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

uploaded_file = st.file_uploader(
    "Upload Soil Test Report",
    type=["pdf"]
)

crop = st.text_input(
    "Crop Name",
    placeholder="Groundnut"
)

if st.button("Analyze Report", use_container_width=True):

    if uploaded_file is None:
        st.warning("Please upload a PDF report.")
        st.stop()

    if not crop.strip():
        st.warning("Please enter the crop name.")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name

    with st.spinner("Analyzing soil report..."):

        try:

            with open(temp_path, "rb") as pdf:

                response = requests.post(
                    f"{API_URL}/analyze",
                    files={
                        "file": (
                            uploaded_file.name,
                            pdf,
                            "application/pdf"
                        )
                    },
                    data={
                        "crop": crop
                    },
                    timeout=300
                )

            os.remove(temp_path)

            st.subheader("API Response")

            st.write("Status Code:", response.status_code)

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis completed successfully!")

                st.json(result)

                report = result.get("report", {})

                recommendations = result.get("recommendations", [])

                st.divider()

                st.header("Farmer Details")

                st.write("Farmer:", report.get("farmer_name"))
                st.write("Crop:", report.get("crop"))
                st.write("Location:", report.get("location"))
                st.write("Sample ID:", report.get("sample_id"))

                st.divider()

                st.header("Soil Parameters")

                if report.get("parameters"):
                    st.dataframe(
                        report["parameters"],
                        use_container_width=True
                    )

                st.divider()

                st.header("Recommendations")

                for rec in recommendations:

                    with st.expander(
                        f"{rec['parameter'].upper()} - {rec['status']}"
                    ):

                        st.write("**Value:**", rec.get("value"))
                        st.write("**Fertilizer:**", rec.get("fertilizer"))
                        st.write("**Dose:**", rec.get("dose"))
                        st.write("**Purpose:**", rec.get("purpose"))
                        st.write("**Application:**", rec.get("application"))
                        st.write("**Precaution:**", rec.get("precaution"))
                        st.write("**Crop Note:**", rec.get("crop_note"))

            else:

                st.error(f"API Error ({response.status_code})")

                try:
                    st.json(response.json())
                except Exception:
                    st.code(response.text)

        except Exception as e:

            st.exception(e)

        finally:

            if os.path.exists(temp_path):
                os.remove(temp_path)