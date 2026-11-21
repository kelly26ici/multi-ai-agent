"""Search the web with Tavily."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_tavily import TavilySearch

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Tavily search tool, keyed from TAVILY_API_KEY."""
    return TavilySearch(max_results=5)
