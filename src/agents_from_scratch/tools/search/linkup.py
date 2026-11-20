"""Search the web with Linkup."""

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
async def linkup_search(query: str) -> str:
    """Search the web with Linkup."""
    response = await client.post(
        "https://api.linkup.so/v1/search",
        headers={
            "Authorization": f"Bearer {settings.linkup_api_key.get_secret_value()}"
        },
        json={"q": query, "depth": "standard", "outputType": "searchResults"},
    )
    return response.text
