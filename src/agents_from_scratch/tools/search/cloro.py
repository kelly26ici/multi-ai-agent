"""Search the web with Cloro."""

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
async def cloro_search(query: str) -> str:
    """Search the web with Cloro."""
    key = settings.cloro_api_key.get_secret_value()
    response = await client.post(
        # TODO: Confirm the endpoint and payload at the Cloro docs.
        "https://api.cloro.ai/search",
        headers={"Authorization": f"Bearer {key}"},
        json={"query": query},
    )
    return response.text
