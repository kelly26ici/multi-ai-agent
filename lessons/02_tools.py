"""Tools: declare, describe, and let the model call them."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# PLAIN TOOL
# =========================================================================


@tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


# =========================================================================
# TOOL WITH A PYDANTIC INPUT
# =========================================================================


class GreetingInput(BaseModel):
    """Input schema for greet."""

    name: str = Field(description="The person to greet.")


@tool
def greet(greeting: GreetingInput) -> str:
    """Greet someone by name."""
    return f"Hello, {greeting.name}."


# =========================================================================
# BINDING
# =========================================================================

tools = [add, greet]
model = init_chat_model(
    settings.default_model,
    api_key=settings.nvidia_api_key.get_secret_value(),
).bind_tools(tools)


if __name__ == "__main__":
    logger.info("Schema for the pydantic tool")
    logger.info(greet.args_schema.model_json_schema())

    logger.info("Model requesting a tool")
    response = model.invoke([HumanMessage("Greet Rex and add 2 plus 3.")])
    for call in response.tool_calls:
        logger.info(call)
        result = {"add": add, "greet": greet}[call["name"]].invoke(call["args"])
        logger.info(ToolMessage(content=str(result), tool_call_id=call["id"]))
