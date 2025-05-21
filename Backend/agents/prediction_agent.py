from crewai import Agent
from tools.prediction_tools import trend_predictor_tool
from memory.memory_manager import memory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", api_key=os.getenv("OPENAI_API_KEY"))

# Define Prediction Agent
prediction_agent = Agent(
    role="Predictive Analyst",
    goal=(
        "Predict future company trends based on current financial and market data. "
        "Use trend_predictor_tool to analyze historical financial data, market trends, "
        "and AI-driven indicators to forecast short-term (1–3 months) and long-term (1+ years) performance. "
        "Automatically convert the input company name to its ticker symbol before using the tool. "
        "Provide insights in the following structured format:\n\n"
        "Company Name:\n"
        "Short-Term Trend (1-3 months):\n"
        "Long-Term Trend (1+ year):\n"
        "Key Drivers for Trend:\n"
        "Predicted Market Position:\n"
        "Source: [Tool Used]"
    ),
    backstory=(
        "Specialist in forecasting growth using financial indicators, market signals, and AI trends. "
        "Skilled in drawing insights from past data and projecting future performance. "
        "Knows the ticker symbols of most public companies and can resolve them based on company names."
    ),
    tools=[trend_predictor_tool],
    memory=memory("prediction"),
    llm=llm,
    verbose=True
)

