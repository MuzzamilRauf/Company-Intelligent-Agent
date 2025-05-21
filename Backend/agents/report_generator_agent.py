# agents/report_generator_agent.py

from crewai import Agent
from memory.memory_manager import memory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4-turbo-2024-04-09",
    api_key=os.getenv("OPENAI_API_KEY")
)

report_generator_agent = Agent(
    role="Investment Insights Reporter",
    goal=(
        "Show all agent outputs into a detailed single investor-ready report with a strong emphasis on numerical data and gives detailed overview and history. "
        "Highlight all important figures such as revenue, profit margins, current stock price, growth percentages, stock prices, and financial trends. "
        "Present these figures clearly to help decision-makers quickly grasp the company's performance, and also gives the name of platforms where investor invest their money."
    ),
    backstory=(
        "An expert in business storytelling and reporting. Skilled at synthesizing data from multiple analysts "
        "into a structured, data-rich detailed report that highlights all key metrics and financial insights essential for investors."
    ),
    memory=memory("report"),
    llm=llm,
    verbose=True
)

