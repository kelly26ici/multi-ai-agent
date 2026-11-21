"""Research subagent: wraps a search-equipped agent as a tool for the supervisor."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.agents.middleware import (
    ModelCallLimitMiddleware,
    ModelRetryMiddleware,
    ToolCallLimitMiddleware,
    ToolRetryMiddleware,
)
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage

from agents_from_scratch.config.prompts import RESEARCHER_PROMPT
from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.search import get_search_tools

# =========================================================================
# SEARCH TOOLS
# =========================================================================

TOOLS = get_search_tools()

# =========================================================================
# RESEARCH SUBAGENT
# =========================================================================

_researcher_agent = create_agent(
    init_chat_model(
        settings.nvidia.models.researcher_model,
        api_key=settings.nvidia.api_key.get_secret_value(),
        temperature=settings.nvidia.temperature.researcher,
    ),
    tools=TOOLS,
    system_prompt=RESEARCHER_PROMPT,
    middleware=[
        ModelCallLimitMiddleware(run_limit=8, exit_behavior="end"),
        ToolCallLimitMiddleware(run_limit=10, exit_behavior="continue"),
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=3),
    ],
)


@tool
async def researcher(query: str) -> str:
    """Research a question using web search and return a concise, sourced answer.

    Use this for any question that needs up-to-date or external information.
    Give it a single, self-contained question. It has no access to the
    conversation history, so include all necessary context in the query.
    """
    result = await _researcher_agent.ainvoke({"messages": HumanMessage(content=query)})
    return result["messages"][-1].content
