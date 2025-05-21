from crewai import Task


def prediction_task_func(company, agent):
    return Task(
        description=(
            f"Use `trend_predictor_tool` to forecast {company}'s performance over short and long-term periods. "
            "Incorporate current financials, industry trends, and risk factors. "
            "Avoid hallucinating unknown data—cite prediction logic."
        ),
        expected_output=(
            "Expected Format:\n"
            "Company: [Name]\n"
            "Short-Term Forecast (6–12 months): ...\n"
            "Long-Term Forecast (2–5 years): ...\n"
            "Growth Drivers: [Market demand, innovation, financials, etc.]\n"
            "Risks: [Regulation, economic conditions, etc.]\n"
            "Confidence Level: High/Medium/Low\n"
            "Source: trend_predictor_tool"
        ),
        agent=agent
    )
