"""Let a small model pick the relevant tools before the main call."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import LLMToolSelectorMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(model: str, **kwargs) -> LLMToolSelectorMiddleware:
    """Return the tool selector middleware."""
    return LLMToolSelectorMiddleware(model=model, **kwargs)
