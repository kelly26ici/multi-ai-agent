"""Search Google with SerpAPI."""

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


class SerpapiSearchInput(BaseModel):
    """Input schema for serpapi_search."""

    query: str = Field(description="The query string to search")


@tool(args_schema=SerpapiSearchInput)
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


# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the SerpAPI search tool."""
    return serpapi_search
