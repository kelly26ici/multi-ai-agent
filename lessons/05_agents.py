"""Agents: create_agent gives you the model-tool loop for free."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# TOOL
# =========================================================================


class AddInput(BaseModel):
    """Input schema for add."""

    a: int = Field(description="The first addend.")
    b: int = Field(description="The second addend.")


@tool
def add(add_input: AddInput) -> int:
    """Add two integers."""
    return add_input.a + add_input.b


# =========================================================================
# AGENT
# =========================================================================

agent = create_agent(
    init_chat_model(
        settings.nvidia.models.default_model,
        api_key=settings.nvidia.api_key.get_secret_value(),
    ),
    tools=[add],
    system_prompt="You answer arithmetic questions with the add tool.",
)


if __name__ == "__main__":
    logger.info("Running a minimal agent")
    result = agent.invoke({"messages": [HumanMessage("What is 41 plus 1?")]})
    logger.info(result["messages"][-1].content)
