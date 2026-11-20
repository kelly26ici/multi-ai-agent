"""Search Google with SerpAPI."""

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
async def serpapi_search(query: str) -> str:
    """Search Google with SerpAPI."""
    response = await client.get(
        "https://serpapi.com/search.json",
        params={
            "engine": "google",
            "q": query,
            "api_key": settings.serpapi_api_key.get_secret_value(),
        },
    )
    return response.text
