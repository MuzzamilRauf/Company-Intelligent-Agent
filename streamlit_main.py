import streamlit as st
from crewai import Crew
from Backend.agents.research_agent import research_agent
from Backend.agents.financial_agent import financial_agent
from Backend.agents.prediction_agent import prediction_agent
from Backend.agents.competitor_agent import competitor_agent
from Backend.agents.report_generator_agent import report_generator_agent
from Backend.tasks.research_task import research_task_func
from Backend.tasks.financial_task import financial_task_func
from Backend.tasks.prediction_task import prediction_task_func
from Backend.tasks.competitor_task import competitor_task_func
from Backend.tasks.report_task import report_task_func
from Backend.memory.memory_manager import memory


# Function to run the full agent workflow
def generate_report(company_name):
    # Initialize all tasks
    research_task = research_task_func(company_name, research_agent)
    financial_task = financial_task_func(company_name, financial_agent)
    prediction_task = prediction_task_func(company_name, prediction_agent)
    competitor_task = competitor_task_func(company_name, competitor_agent)
    report_task = report_task_func(company_name, report_generator_agent)

    # Create and execute Crew
    crew = Crew(
        agents=[
            research_agent,
            financial_agent,
            competitor_agent,
            prediction_agent,
            report_generator_agent
        ],
        tasks=[
            research_task,
            financial_task,
            competitor_task,
            prediction_task,
            report_task
        ],
        verbose=True
    )

    # Save user query in memory
    memory("research").chat_memory.add_user_message(f"Research the background of {company_name}")

    # Run agents and generate report
    final_result = crew.kickoff()
    final_report = str(final_result)

    # Save to markdown file
    file_path = "Backend/generated_report.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_report)

    return final_report, file_path


# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="Investment Research Report", layout="wide")
st.title("📈 Investment Intelligence Report Generator")

st.markdown("""
Welcome to the **Investment Intelligence Report Generator** powered by AI agents.
Enter a company name below and get a detailed investment report backed by financial data, market trends, and predictive analytics.
""")

# Session state for input
if "company_input" not in st.session_state:
    st.session_state.company_input = ""

# Text input with value from session state
company_input = st.text_input(
    "🔎 Enter the company name you want to research:",
    placeholder="e.g., Tesla, Apple, Amazon",
    value=st.session_state.company_input
)
st.session_state.company_input = company_input  # Always update session state

# Generate report only once
if company_input and "report_text" not in st.session_state:
    with st.spinner("Generating report... please wait ⏳"):
        report_text, report_file_path = generate_report(company_input)
        st.session_state.report_text = report_text
        st.session_state.report_file_path = report_file_path
        st.session_state.last_company = company_input

# Display report and download button if available
if "report_text" in st.session_state and st.session_state.last_company == company_input:
    st.subheader(f"📄 Investment Report for {company_input}")
    st.markdown(st.session_state.report_text, unsafe_allow_html=True)

    # Download Button
    with open(st.session_state.report_file_path, "rb") as f:
        st.download_button("📥 Download Report", f, file_name=f"{company_input}_Investment_Report.md")

    # New Report Button
    if st.button("🔄 New Report"):
        for key in ["report_text", "report_file_path", "last_company", "company_input"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()