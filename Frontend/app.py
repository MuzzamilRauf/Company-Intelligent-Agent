import streamlit as st
import requests

st.set_page_config(page_title="Investment Research Report", layout="wide")
st.title("📈 Investment Intelligence Report Generator")

st.markdown("""
Welcome to the **Investment Intelligence Report Generator** powered by AI agents.
Enter a company name below and get a detailed investment report backed by financial data, market trends, and predictive analytics.
""")

# Preserve company input across reruns
if "company_input" not in st.session_state:
    st.session_state.company_input = ""

company_input = st.text_input(
    "🔎 Enter the company name you want to research:",
    placeholder="e.g., Tesla, Apple, Amazon",
    value=st.session_state.company_input
)
st.session_state.company_input = company_input

# Clear report if input changes
if "last_company" in st.session_state and st.session_state.last_company != company_input:
    for key in ["report_text", "report_file_path", "last_company"]:
        st.session_state.pop(key, None)

# Trigger report generation
if company_input and "report_text" not in st.session_state:
    with st.spinner("Generating report... please wait ⏳"):
        try:
            # response = requests.post(
            #     "http://backend:8000/generate-report",
            #     json={"company_name": company_input},
            #     timeout=600  # ⏱️ Optional: Long timeout for complex generation
            # )

            response = requests.post(
                "http://localhost:8000/generate-report",
                json={"company_name": company_input},
                timeout=600
            )
            response.raise_for_status()
            data = response.json()
            st.session_state.report_text = data["report_text"]
            st.session_state.report_file_path = data["report_file_path"]
            st.session_state.last_company = company_input
        except requests.exceptions.RequestException as e:
            st.error(f"🚨 Failed to generate report: {e}")

# Show report if available
if "report_text" in st.session_state and st.session_state.last_company == company_input:
    st.subheader(f"📄 Investment Report for {company_input}")
    st.markdown(st.session_state.report_text, unsafe_allow_html=True)

    try:
        with open(st.session_state.report_file_path, "rb") as f:
            st.download_button(
                "📥 Download Report",
                f,
                file_name=f"{company_input}_Investment_Report.md",
                mime="text/markdown"
            )
    except FileNotFoundError:
        st.warning("⚠️ Report file not found. Please retry.")

    if st.button("🔄 New Report"):
        for key in ["report_text", "report_file_path", "last_company", "company_input"]:
            st.session_state.pop(key, None)
        st.experimental_rerun()

