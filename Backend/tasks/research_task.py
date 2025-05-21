from crewai import Task


def research_task_func(company, agent):
    return Task(
        description=(
            f"Perform comprehensive research on {company} using `search_tool`. "
            "Extract reliable company background, mission, services, and recent developments from credible sources."
        ),
        expected_output=(
            "Expected Format:\n"
            "Company Name: ...\n"
            "Founded: ... | Founders: ... | HQ: ...\n"
            "Mission & Vision: ...\n"
            "Products/Services: ...\n"
            "Recent News: ... (within last 6 months)\n"
            "Source: search_tool"
        ),
        agent=agent
    )
