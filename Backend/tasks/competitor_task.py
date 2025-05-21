from crewai import Task


def competitor_task_func(company, agent):
    return Task(
        description=(
            f"Perform a detailed competitive analysis for {company} using `competitor_search_tool`. "
            "Identify and analyze the 8 direct competitors. Focus on key dimensions such as products, pricing, business strategy, market share, revenue, employee count, and headquarters location. "
            "Summarize competitive positioning with strategic insights. "
            "Ensure all insights are factual and sourced from the tool. Avoid hallucinating information."
        ),
        expected_output=(
            "Expected Output Format:\n\n"
            "Target Company: [Company Name]\n\n"
            "Top Competitors:\n"
            "| Company        | Sector        | Market Share | Revenue   | Employees | HQ Location        |\n"
            "|----------------|---------------|--------------|-----------|-----------|--------------------|\n"
            "| Competitor A   | Tech          | 15%          | $50B      | 80,000    | New York, NY       |\n"
            "| Competitor B   | Tech          | 10%          | $35B      | 45,000    | San Francisco, CA  |\n"
            "| Competitor C   | Tech          | 8%           | $25B      | 30,000    | Seattle, WA        |\n\n"

            "Strengths and Weaknesses:\n"
            "| Company        | Strengths                         | Weaknesses                     |\n"
            "|----------------|------------------------------------|--------------------------------|\n"
            "| Competitor A   | R&D investment, strong branding    | High operational costs         |\n"
            "| Competitor B   | Agile pricing, fast market entry   | Limited international presence |\n"
            "| Competitor C   | Loyal customer base, innovation    | Declining margins              |\n\n"

            "Strategic Insights:\n"
            "- Trend: Competitors investing heavily in AI and automation.\n"
            "- Opportunity: Gaps in mid-market offerings.\n"
            "- Threat: Price war initiated by Competitor B.\n\n"

            "Source: [competitor_search_tool or verified source]"
        ),
        agent=agent
    )

