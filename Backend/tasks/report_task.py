from crewai import Task

def report_task_func(company, agent):
    return Task(
        description=(
            f"Using the outputs from the research, financial, competitor, and prediction analysts, "
            f"write a final structured detailed report for {company}. Organize it with clear sections using headers, bullet points, and tables where appropriate. "
            f"Emphasize specific figures, such as revenue, profit margins, growth rates, stock trends, and competitive metrics. "
            f"For the competitor section, include tabular comparisons with fields like Company, Sector, Market Share, Revenue, Employees, HQ Location, Strengths, and Weaknesses. "
            f"Ensure that each section flows logically and builds a coherent investment case for or against the company."
        ),
        expected_output=(
            "A complete, structured company report including:\n\n"
            "1. **Company Overview** (from Research Analyst):\n"
            "   - Background, mission, core business, and recent highlights.\n\n"
            "2. **Financial Summary** (from Financial Analyst):\n"
            "   - Key metrics: Revenue Growth, YoY Growth, Market Cap, Profit Margins, Stock Price Trends.\n"
            "   - Current Price, 52 Week High, 52 Week Low"
            "   - Include financial KPIs in bullet points or table format.\n\n"
            "3. **Competitor Landscape** (from Competitor Analyst):\n"
            "   - Include two markdown-style tables:\n"
            "     a. **Competitor Overview Table**:\n"
            "     | Company        | Sector |  Market Cap   | Revenue | Employees | HQ Location        |\n"
            "     |----------------|--------|---------------|---------|-----------|--------------------|\n"
            "     | Competitor A   | ...    | ...           | ...     | ...       | ...                |\n"
            "     | Competitor B   | ...    | ...           | ...     | ...       | ...                |\n\n"
            "     b. **Stock History**:\n"
            "     | Company        | Current Price   |  52 Week High   |  52 Week Low      |\n"
            "     |----------------|-----------------|-----------------|-------------------|\n"
            "     | Competitor A   | ...             | ...             | ...               |\n"
            "     | Competitor B   | ...             | ...             | ...               |\n\n"
            "     c. **Strengths and Weaknesses Table**:\n"
            "     | Company        | Strengths                       | Weaknesses                   |\n"
            "     |----------------|----------------------------------|------------------------------|\n"
            "     | Competitor A   | ...                              | ...                          |\n"
            "     | Competitor B   | ...                              | ...                          |\n\n"
            "4. **Growth & Risk Forecast** (from Prediction Analyst):\n"
            "   - Include historical stock price (30 days), current price, predicted price, and expected growth rates.\n"
            "   - Mention forecasted revenue and net income with percentages.\n\n"
            "5. **Final Recommendations or Insights**:\n"
            "   - Summary of all findings.\n"
            "   - Clear recommendation backed by data (e.g., Buy/Hold/Sell).\n"
        ),
        agent=agent
    )



