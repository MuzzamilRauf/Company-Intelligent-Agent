import requests
from crewai.tools import tool
# from langchain_core.tools import tool


@tool("competitor_search_tool")
def competitor_search_tool(company_name: str) -> str:
    """Search for top competitors of a company using Serper (abcproxy.com) and return results as formatted string."""
    query = f"{company_name} top competitors"

    params = {
        "engine": "google",
        "q": query,
        "api_key": "#########################",  # Use env var if available
        "fetch_mode": "static",
    }

    response = requests.get("https://serpapi.abcproxy.com/search", params=params)
    data = response.json()

    organic_results = data.get('data', {}).get('organic_results', [])
    if not organic_results:
        return "No search results found."

    results_text = "\nTop Search Results:\n"
    for result in organic_results:
        title = result.get('title', 'No title')
        url = result.get('url', 'No URL')
        description = result.get('description', 'No description')
        results_text += f"• {title}\n  {description}\n  URL: {url}\n\n"

    return results_text

# print(competitor_search_tool("Toyota"))


