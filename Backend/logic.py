from crewai import Crew
from agents.research_agent import research_agent
from agents.financial_agent import financial_agent
from agents.prediction_agent import prediction_agent
from agents.competitor_agent import competitor_agent
from agents.report_generator_agent import report_generator_agent
from tasks.research_task import research_task_func
from tasks.financial_task import financial_task_func
from tasks.prediction_task import prediction_task_func
from tasks.competitor_task import competitor_task_func
from tasks.report_task import report_task_func
from memory.memory_manager import memory


def generate_report(company_name: str):
    research_task = research_task_func(company_name, research_agent)
    financial_task = financial_task_func(company_name, financial_agent)
    prediction_task = prediction_task_func(company_name, prediction_agent)
    competitor_task = competitor_task_func(company_name, competitor_agent)
    report_task = report_task_func(company_name, report_generator_agent)

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

    memory("research").chat_memory.add_user_message(f"Research the background of {company_name}")

    final_result = crew.kickoff()
    final_report = str(final_result)

    file_path = "generated_report.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_report)

    return final_report, file_path