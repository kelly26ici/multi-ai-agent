"""Search the web with Keenable."""

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
async def keenable_search(query: str) -> str:
    """Search the web with Keenable."""
    key = settings.keenable_api_key.get_secret_value()
    response = await client.post(
        # TODO: Confirm the endpoint and payload at https://docs.keenable.ai.
        "https://api.keenable.ai/search",
        headers={"Authorization": f"Bearer {key}"},
        json={"query": query},
    )
    return response.text
