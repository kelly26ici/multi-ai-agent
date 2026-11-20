"""Search the web with Querit."""

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
async def querit_search(query: str) -> str:
    """Search the web with Querit."""
    key = settings.querit_api_key.get_secret_value()
    response = await client.post(
        # TODO: Confirm the endpoint and payload at https://querit.com/docs.
        "https://api.querit.com/v1/search",
        headers={"Authorization": f"Bearer {key}"},
        json={"query": query},
    )
    return response.text
