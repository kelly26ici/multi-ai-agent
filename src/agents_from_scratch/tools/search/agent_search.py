"""Search the web with AgentSearch."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.core.clients import client

# =========================================================================
# TOOL
# =========================================================================


class AgentSearchInput(BaseModel):
    """Input schema for agent_search."""

    query: str = Field(description="The query string to search")


@tool(args_schema=AgentSearchInput)
async def agent_search(query: str) -> str:
    """Search the web with the free AgentSearch tier."""
    response = await client.post(
        "https://api.agentsearchhq.com/search",
        json={"query": query},
    )
    return response.text


# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the AgentSearch tool."""
    return agent_search
