from crewai.tools import tool
import requests

@tool("search_tool")
def search_tool(query: str) -> str:
    """Search for a query using Serper (abcproxy.com) and return the first snippet."""

    params = {
        "engine": "google",
        "q": query,
        "api_key": "##############################",  # You can replace this with os.getenv(...)
        "fetch_mode": "static",
    }

    response = requests.get("https://serpapi.abcproxy.com/search", params=params)
    data = response.json()

    try:

        organic_results = data.get('data', {}).get('organic_results', [])
        if not organic_results:
            return "No search results found."

        results_text = "\nTop Search Results:\n"
        for result in organic_results:
            title = result.get('title', 'No title')
            url = result.get('url', 'No URL')
            description = result.get('description', 'No description')
            # favicon = result.get('favicon', '')
            origin_navigation = result.get('origin_navigation', 'N/A')  # For articles, research, etc.
            origin_site = result.get('origin_site', 'N/A')  # Article, blog, PDF, etc.
            site_links = result.get('site_links', 'N/A')  # Engagement metrics if available

            results_text += (
                f"  Title: {title}\n"
                f"  Description: {description}\n"
                f"  URL: {url}\n"
                # f"  Favicon: {favicon}\n"
                f"  Origin_navigation: {origin_navigation}\n"
                f"  Origin_site: {origin_site}\n"
                f"  Site_links: {site_links}\n\n"

            )

        return results_text

    except (KeyError, IndexError):
        return "No results found."
    except Exception as e:
        return f"Error occurred: {e}"

# def search_tool(query: str) -> str:
#     """Search for a query using Serper (abcproxy.com) and return the first snippet."""
#
#     params = {
#         "engine": "google",
#         "q": query,
#         "api_key": "fec739be5d70e943fe22b4954cb4e018",  # You can replace this with os.getenv(...)
#         "fetch_mode": "static",
#     }
#
#     try:
#         response = requests.get("https://serpapi.abcproxy.com/search", params=params)
#         data = response.json()

##########################################################################
        # This piece of code return the total no of lists in the return json data of serp api

        # main_data = data.get('data', {})
        # for key, value in main_data.items():
        #     print(f"{key}: {type(value)}")

##########################################################################
        # This piece of code will return each key and value of each dictionary of each list with iteration of loop

        # main_data = data.get('data', {})
        #
        # for key, value in main_data.items():
        #     print(f"\nList Name: {key} (Type: {type(value)})")
        #
        #     if isinstance(value, list):
        #         for i, item in enumerate(value):
        #             if isinstance(item, dict):
        #                 print(f"  Item {i + 1}:")
        #                 for sub_key, sub_val in item.items():
        #                     print(f"    {sub_key}: {sub_val}")
        #             else:
        #                 print(f"  Item {i + 1}: {item}")
        #     elif isinstance(value, dict):
        #         print("  Dictionary contents:")
        #         for sub_key, sub_val in value.items():
        #             print(f"    {sub_key}: {sub_val}")
        #     else:
        #         print(f"  Value: {value}")

#################################################################################

#         organic_results = data.get('data', {}).get('organic_results', [])
#         if not organic_results:
#             return "No search results found."
#
#         results_text = "\nTop Search Results:\n"
#         for result in organic_results:
#             title = result.get('title', 'No title')
#             url = result.get('url', 'No URL')
#             description = result.get('description', 'No description')
#             favicon = result.get('favicon', '')
#             origin_navigation = result.get('origin_navigation', 'N/A')  # For articles, research, etc.
#             origin_site = result.get('origin_site', 'N/A')  # Article, blog, PDF, etc.
#             site_links = result.get('site_links', 'N/A')  # Engagement metrics if available
#
#             results_text += (
#                 f"  Title: {title}\n"
#                 f"  Description: {description}\n"
#                 f"  URL: {url}\n"
#                 f"  Favicon: {favicon}\n"
#                 f"  Origin_navigation: {origin_navigation}\n"
#                 f"  Origin_site: {origin_site}\n"
#                 f"  Site_links: {site_links}\n\n"
#
#             )
#
#
#         return results_text
#
#     except (KeyError, IndexError):
#         return "No results found."
#     except Exception as e:
#         return f"Error occurred: {e}"
#
#
# print(search_tool("Google"))