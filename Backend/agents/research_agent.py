from crewai import Agent
from tools.search_tools import search_tool
from memory.memory_manager import memory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", api_key=os.getenv("OPENAI_API_KEY"))

# Define Research Agent
research_agent = Agent(
    role="Research Analyst",
    goal=(
        "Gather accurate and detailed company background information using web-based research tools. "
        "Use search_tool to extract key company facts such as company history, key people, mission, industry, "
        "and other relevant details. Ensure results are in the following structured format:\n\n"
        "Company Name:\n"
        "Founded: [Year]\n"
        "Industry: [Industry]\n"
        "Key People: [Founder(s), CEO, etc.]\n"
        "Mission Statement: [Company Mission]\n"
        "Company Bio: [Overview of the company’s business]\n"
        "Source: [Tool Used]"
    ),
    backstory=(
        "An expert in web research, financial blogs, Wikipedia, and company bios, skilled at extracting relevant data."
    ),
    tools=[search_tool],
    memory=memory("research"),
    llm=llm,
    verbose=True
)
