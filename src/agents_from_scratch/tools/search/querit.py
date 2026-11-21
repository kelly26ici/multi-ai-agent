"""Search the web with Querit."""

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


class QueritSearchInput(BaseModel):
    """Input schema for querit_search."""

    query: str = Field(description="The query string to search")


@tool(args_schema=QueritSearchInput)
async def querit_search(query: str) -> str:
    """Search the web with Querit."""
    response = await client.post(
        "https://api.querit.com/v1/search",
        headers={
            "Authorization": f"Bearer {settings.querit_api_key.get_secret_value()}"
        },
        json={"query": query},
    )
    return response.text


# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Querit search tool."""
    return querit_search
