"""Cap how many model calls an agent may make."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ModelCallLimitMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(**kwargs) -> ModelCallLimitMiddleware:
    """Return the model call limit middleware."""
    return ModelCallLimitMiddleware(run_limit=8, exit_behavior="error", **kwargs)
