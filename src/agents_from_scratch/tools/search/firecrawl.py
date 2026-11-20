"""Search the web with Firecrawl."""

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
async def firecrawl_search(query: str) -> str:
    """Search the web with Firecrawl."""
    response = await client.post(
        "https://api.firecrawl.dev/v2/search",
        headers={
            "Authorization": f"Bearer {settings.firecrawl_api_key.get_secret_value()}"
        },
        json={"query": query, "sources": [{"type": "web"}], "limit": 5},
    )
    return response.text
