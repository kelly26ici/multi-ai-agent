"""Tool groups: email, calendar, search, crawl, and all of them together."""

# =========================================================================
# IMPORTS
# =========================================================================

from agents_from_scratch.tools.calendar import calendar_tools
from agents_from_scratch.tools.crawl import crawl_tools
from agents_from_scratch.tools.email import email_tools
from agents_from_scratch.tools.search import get_search_tools

# =========================================================================
# GROUP
# =========================================================================

search_tools = get_search_tools()

__all__ = [
    "calendar_tools",
    "crawl_tools",
    "email_tools",
    "get_all_tools",
    "search_tools",
]


def get_all_tools() -> list:
    """Return every tool the assistant can use."""
    return [*email_tools, *calendar_tools, *crawl_tools, *search_tools]
