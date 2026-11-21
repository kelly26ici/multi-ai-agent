"""Email subagent: wraps an email-writing agent as a tool for the supervisor."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.agents.middleware import (
    ModelCallLimitMiddleware,
    ModelRetryMiddleware,
)
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage

from agents_from_scratch.config.prompts import WRITER_PROMPT
from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.email import write_email

# =========================================================================
# AGENT
# =========================================================================

# Built once at import time and reused for every call.
_email_agent = create_agent(
    model=init_chat_model(
        settings.nvidia.models.email_writer_model,
        api_key=settings.nvidia.api_key.get_secret_value(),
        temperature=settings.nvidia.temperature.email_writer,
    ),
    tools=[write_email],
    system_prompt=WRITER_PROMPT,
    middleware=[
        ModelCallLimitMiddleware(run_limit=5, exit_behavior="end"),
        ModelRetryMiddleware(max_retries=2),
    ],
)


@tool
async def email_writer(request: str) -> str:
    """Write and send an email based on a plain-language request.

    Use this whenever the user wants an email drafted or sent. Include
    everything the writer needs in the request: recipient, subject or
    purpose, key points, tone, and any details to mention. The writer has
    no access to the conversation history.
    """
    result = await _email_agent.ainvoke({"messages": [HumanMessage(content=request)]})
    return result["messages"][-1].content
