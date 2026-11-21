"""Crawl a site with Firecrawl."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_firecrawl import FirecrawlCrawl

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Firecrawl crawl tool."""
    return FirecrawlCrawl(api_key=settings.firecrawl_api_key.get_secret_value())
