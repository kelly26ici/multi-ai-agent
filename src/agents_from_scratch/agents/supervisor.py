"""Supervisor agent: delegates to the researcher and the email writer."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.agents.middleware import (
    HumanInTheLoopMiddleware,
    ModelCallLimitMiddleware,
    ModelRetryMiddleware,
)
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

from agents_from_scratch.agents.email_writer import email_writer
from agents_from_scratch.agents.researcher import researcher
from agents_from_scratch.config.prompts import SUPERVISOR_PROMPT
from agents_from_scratch.config.settings import settings

# =========================================================================
# AGENT
# =========================================================================

agent = create_agent(
    model=init_chat_model(
        settings.nvidia.models.supervisor_model,
        api_key=settings.nvidia.api_key.get_secret_value(),
        temperature=settings.nvidia.temperature.supervisor,
    ),
    tools=[researcher, email_writer],
    system_prompt=SUPERVISOR_PROMPT,
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(interrupt_on={"email_writer": True}),
        ModelCallLimitMiddleware(run_limit=15, exit_behavior="end"),
        ModelRetryMiddleware(max_retries=2),
    ],
)
