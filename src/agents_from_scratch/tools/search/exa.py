"""Search the web with Exa."""

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
async def exa_search(query: str) -> str:
    """Search the web with Exa."""
    response = await client.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": settings.exa_api_key.get_secret_value()},
        json={"query": query, "type": "auto", "contents": {"highlights": True}},
    )
    return response.text
