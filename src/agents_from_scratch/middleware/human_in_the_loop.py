"""Pause the agent until a human approves a tool call."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import HumanInTheLoopMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(interrupt_on: dict, **kwargs) -> HumanInTheLoopMiddleware:
    """Return the human-in-the-loop middleware."""
    return HumanInTheLoopMiddleware(interrupt_on=interrupt_on, **kwargs)
