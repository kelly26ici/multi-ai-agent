"""Retry failed tool calls with backoff."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ToolRetryMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(**kwargs) -> ToolRetryMiddleware:
    """Return the tool retry middleware."""
    return ToolRetryMiddleware(max_retries=3, **kwargs)
