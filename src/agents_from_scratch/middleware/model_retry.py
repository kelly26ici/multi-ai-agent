"""Retry failed model calls with backoff."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ModelRetryMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(**kwargs) -> ModelRetryMiddleware:
    """Return the model retry middleware."""
    return ModelRetryMiddleware(max_retries=3, **kwargs)
