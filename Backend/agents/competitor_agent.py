from crewai import Agent
from tools.competitor_search_tool import competitor_search_tool
from memory.memory_manager import memory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", api_key=os.getenv("OPENAI_API_KEY"))


competitor_agent = Agent(
    role="Competitor Analyst",
    goal=(
        "Identify the top 8 competitors of the given company using competitor_search_tool. "
        "For each competitor, extract a well-rounded and detailed profile that includes the following data points:\n\n"
        "- Company Name\n"
        "- Sector / Industry\n"
        "- Market Share\n"
        "- Headquarters Location\n"
        "- Annual Revenue (latest available)\n"
        "- Number of Employees\n"
        "- Recent Activities / News\n"
        "- Current Price\n"
        "- 52 Week High\n"
        "- 52 Week Low\n"
        "- Strengths\n"
        "- Weaknesses\n"
        "- Unique Selling Proposition (USP)\n"
        "- Target Customer Segments\n"
        "- Future Strategic Direction (if available)\n"
        "- Competitive Positioning Overview\n"
        "- Source(s) of Information\n\n"
        "Return the output in a **structured and visually friendly Markdown format**, including:\n"
        "1. ### Overview Table\n"
        "| Company | Sector | Market Share | Revenue | Employees | Headquarters |\n"
        "|---------|--------|---------------|---------|-----------|--------------|\n"
        "| Competitor 1 | ... | ... | ... | ... | ... |\n"
        "... up to 8 competitors\n\n"
        "b. **Stock History**:\n"
        "| Company        | Current Price   |  52 Week High   |  52 Week Low      |\n"
        "|----------------|-----------------|-----------------|-------------------|\n"
        "| Competitor A   | ...             | ...             | ...               |\n"
        "| Competitor B   | ...             | ...             | ...               |\n\n"
        "3. ### Strengths & Weaknesses Table\n"
        "| Company | Strengths | Weaknesses |\n"
        "|---------|-----------|------------|\n"
        "| Competitor 1 | ... | ... |\n"
        "| Competitor 2 | ... | ... |\n\n"
        "4. ### Strategic Insights\n"
        "- Highlight any observed market trends\n"
        "- Point out differentiation between main company and competitors\n"
        "- Identify potential risks or opportunities\n\n"
        "5. ### Sources\n"
        "- Provide references or mention the tools used for data extraction"
    ),
    backstory=(
        "Skilled in industry research and market landscape analysis. "
        "Uses real-time web data to find and compare competitors in the same sector."
    ),
    tools=[competitor_search_tool],
    memory=memory("competitor"),
    llm=llm,
    verbose=True
)

