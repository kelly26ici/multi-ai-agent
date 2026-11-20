"""Extract structured data with Diffbot."""

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
async def diffbot_search(query: str) -> str:
    """Search the web with the Diffbot knowledge graph."""
    response = await client.get(
        "https://api.diffbot.com/v3/analyze",
        params={
            "token": settings.diffbot_api_key.get_secret_value(),
            "type": "search",
            "q": query,
        },
    )
    return response.text
