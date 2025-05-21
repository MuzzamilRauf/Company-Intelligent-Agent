from crewai import Task


def financial_task_func(company, agent):
    return Task(
        description=(
            f"Analyze {company}'s financial status using the `get_financial_summary` tool. "
            "Extract real-time stock data, revenue growth, and profitability metrics. "
            "Ensure insights are fact-based with no assumptions."
        ),
        expected_output=(
            "Expected Format:\n"
            "Company: [Name]\n"
            "1. Stock History (1M, 6M, 1Y): ...\n"
            "2. Market Cap: ...\n"
            "3. Revenue Growth: ...\n"
            "4. P/E Ratio: ...\n"
            "5. Financial Summary/Health Grade\n"
            "Source: get_financial_summary"
        ),
        agent=agent
    )
