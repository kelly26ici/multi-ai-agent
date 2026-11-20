"""Crawl a page into markdown with Firecrawl."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.tools import tool

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.clients import client

# =========================================================================
# TOOL
# =========================================================================


@tool
async def firecrawl_crawl(url: str) -> str:
    """Scrape a page into markdown with Firecrawl."""
    response = await client.post(
        "https://api.firecrawl.dev/v2/scrape",
        headers={
            "Authorization": f"Bearer {settings.firecrawl_api_key.get_secret_value()}"
        },
        json={"url": url, "formats": ["markdown"], "onlyMainContent": True},
    )
    return response.text
