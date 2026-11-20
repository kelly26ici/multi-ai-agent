"""Search the web with AgentSearch."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.tools import tool

from agents_from_scratch.core.clients import client

# =========================================================================
# TOOL
# =========================================================================


@tool
async def agent_search(query: str) -> str:
    """Search the web with the free AgentSearch tier."""
    response = await client.post(
        # TODO: Confirm the endpoint and payload at https://agentsearchhq.com.
        "https://api.agentsearchhq.com/search",
        json={"query": query},
    )
    return response.text
