"""Summarize old messages before the context overflows."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import SummarizationMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(model: str, **kwargs) -> SummarizationMiddleware:
    """Return the summarization middleware."""
    return SummarizationMiddleware(model=model, trigger=("messages", 40), **kwargs)
