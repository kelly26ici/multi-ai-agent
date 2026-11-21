"""Search the web with Cloro."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.clients import client

# =========================================================================
# TOOL
# =========================================================================


class CloroSearchInput(BaseModel):
    """Input schema for cloro_search."""

    query: str = Field(description="The query string to search")


@tool(args_schema=CloroSearchInput)
async def cloro_search(query: str) -> str:
    """Search the web with Cloro."""
    response = await client.post(
        "https://api.cloro.ai/search",
        headers={
            "Authorization": f"Bearer {settings.cloro_api_key.get_secret_value()}"
        },
        json={"query": query},
    )
    return response.text


# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Cloro search tool."""
    return cloro_search
