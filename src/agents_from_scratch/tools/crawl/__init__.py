"""Crawl tools."""

# =========================================================================
# IMPORTS
# =========================================================================

from loguru import logger

from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.crawl import firecrawl

# =========================================================================
# GROUP
# =========================================================================


def get_crawl_tools() -> list:
    """Return the crawl tools whose API keys are configured."""
    if settings.firecrawl_api_key is None:
        logger.warning("firecrawl_api_key is not set; skipping the crawl tool")
        return []
    return [firecrawl.get_tool()]


crawl_tools = get_crawl_tools()

__all__ = ["crawl_tools", "get_crawl_tools"]
