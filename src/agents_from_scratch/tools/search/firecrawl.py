"""Search the web with Firecrawl."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_firecrawl import FirecrawlSearch

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Firecrawl search tool."""
    return FirecrawlSearch(api_key=settings.firecrawl_api_key.get_secret_value())
