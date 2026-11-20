"""Middleware: wrap model calls without touching agent code."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.agents.middleware import (
    ModelCallLimitMiddleware,
    SummarizationMiddleware,
)
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# TOOL
# =========================================================================


class UpperInput(BaseModel):
    """Input schema for shout."""

    text: str = Field(description="The text to uppercase.")


@tool
def shout(text_input: UpperInput) -> str:
    """Uppercase the given text."""
    return text_input.text.upper()


# =========================================================================
# AGENT WITH MIDDLEWARE
# =========================================================================

model = init_chat_model(
    settings.default_model,
    api_key=settings.nvidia_api_key.get_secret_value(),
)

agent = create_agent(
    model=model,
    tools=[shout],
    system_prompt="You shout what the user writes.",
    middleware=[
        ModelCallLimitMiddleware(run_limit=8, exit_behavior="error"),
        SummarizationMiddleware(model=model, trigger=("messages", 40)),
    ],
)


if __name__ == "__main__":
    logger.info("Running an agent guarded by middleware")
    logger.info(agent.invoke({"messages": [HumanMessage("Shout: i am learning")]}))
