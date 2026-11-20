"""Agent that delegates to the researcher and the writer."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool

from agents_from_scratch.agents.researcher import agent as researcher
from agents_from_scratch.agents.writer import agent as writer
from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.calendar_tools import (
    check_calendar_availability,
    schedule_meeting,
)
from agents_from_scratch.tools.email_tools import Question, write_email

# =========================================================================
# SUBAGENT TOOLS
# =========================================================================


@tool
async def research(question: str) -> str:
    """Ask the researcher a question."""
    state = await researcher.ainvoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    return state["messages"][-1].content


@tool
async def draft(notes: str) -> str:
    """Ask the writer to draft an e-mail from notes."""
    state = await writer.ainvoke({"messages": [{"role": "user", "content": notes}]})
    return state["messages"][-1].content


# =========================================================================
# AGENT
# =========================================================================

agent = create_agent(
    init_chat_model(
        settings.default_model,
        api_key=settings.nvidia_api_key.get_secret_value(),
    ),
    tools=[
        research,
        draft,
        write_email,
        schedule_meeting,
        check_calendar_availability,
        Question,
    ],
    system_prompt="You delegate research and drafting, then act on the results.",
)
