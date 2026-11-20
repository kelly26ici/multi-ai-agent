"""Search the web with CrustAPI."""

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
async def crustapi_search(query: str) -> str:
    """Search the web with CrustAPI."""
    key = settings.crustapi_api_key.get_secret_value()
    response = await client.post(
        # TODO: Confirm the endpoint and payload at https://crustapi.com/docs.
        "https://api.crustapi.com/search",
        headers={"Authorization": f"Bearer {key}"},
        json={"query": query},
    )
    return response.text
