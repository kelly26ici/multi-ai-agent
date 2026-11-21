"""Search Google surfaces with CrustAPI."""

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


class CrustapiSearchInput(BaseModel):
    """Input schema for crustapi_search."""

    query: str = Field(description="The query string to search")
    surface: str = Field(
        default="news",
        description="Google surface to query: maps, places, news, shopping, images, scholar, or patents.",
    )


@tool(args_schema=CrustapiSearchInput)
async def crustapi_search(query: str, surface: str = "news") -> str:
    """Search a Google surface with CrustAPI."""
    response = await client.get(
        "https://crustapi.com/v1/search",
        params={"type": surface, "q": query},
        headers={"x-api-key": settings.crustapi_api_key.get_secret_value()},
    )
    return response.text


# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the CrustAPI search tool."""
    return crustapi_search
