from crewai import Agent
from tools.finance_tools import get_financial_summary
from memory.memory_manager import memory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", api_key=os.getenv("OPENAI_API_KEY"))

# Define Financial Agent
financial_agent = Agent(
    role="Financial Analyst",
    goal=(
        "Given a company name, first identify its stock ticker symbol using your financial knowledge. "
        "Then analyze the company's financial health and stock performance using the get_financial_summary tool. "
        "Extract financial indicators such as revenue, YoY growth, profit margins, and stock performance. "
        "Present the analysis in the following structured format:\n\n"
        "Company Name:\n"
        "Ticker Symbol:\n"
        "Revenue:\n"
        "YoY Growth:\n"
        "Profit Margin:\n"
        "Stock Performance (1 month/6 months/1 year):\n"
        "Key Financial Insights:\n"
        "Source: [Tool Used]"
    ),
    backstory=(
        "You are a financial expert skilled in identifying public companies' ticker symbols and analyzing their "
        "financial data using tools like Yahoo Finance."
    ),
    tools=[get_financial_summary],
    memory=memory("financial"),
    llm=llm,
    verbose=True
)

