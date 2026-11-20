"""Agent that researches questions with search tools."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool

from agents_from_scratch.config.prompts import RESEARCHER_PROMPT
from agents_from_scratch.config.settings import settings

# =========================================================================
# SEARCH TOOL
# =========================================================================


@tool
async def search(query: str) -> str:
    """Search the web for the query."""
    from agents_from_scratch.tools.search import exa

    return await exa.exa_search(query)


# =========================================================================
# R:quita AGENT
# =========================================================================

agent = create_agent(
    init_chat_model(
        settings.default_model,
        api_key=settings.nvidia_api_key.get_secret_value(),
    ),
    tools=[search],
    system_prompt=RESEARCHER_PROMPT,
)
