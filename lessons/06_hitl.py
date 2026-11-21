"""Human-in-the-loop: pause before a tool runs, then resume with a decision."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# TOOL
# =========================================================================


def cancel_flight(flight_id: str) -> str:
    """Cancel a flight."""
    return f"Flight {flight_id} cancelled."


# =========================================================================
# AGENT
# =========================================================================

agent = create_agent(
    init_chat_model(
        settings.nvidia.models.default_model,
        api_key=settings.nvidia.api_key.get_secret_value(),
    ),
    tools=[cancel_flight],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={"cancel_flight": {"allowed_decisions": ["approve", "reject"]}}
        )
    ],
    checkpointer=MemorySaver(),
)


if __name__ == "__main__":
    logger.info("Turn 1: the run pauses on the tool call")
    config = {"configurable": {"thread_id": "hitl-demo"}}
    paused = agent.invoke(
        {"messages": [HumanMessage("Cancel flight BA249.")]}, config=config
    )
    logger.info(paused["__interrupt__"])

    logger.info("Turn 2: resume with the approval")
    approved = agent.invoke(
        Command(resume={"decisions": [{"type": "approve"}]}), config=config
    )
    logger.info(approved["messages"][-1].content)
