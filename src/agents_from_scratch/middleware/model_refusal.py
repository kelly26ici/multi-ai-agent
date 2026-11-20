"""Treat a model refusal as an error instead of an answer."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ModelRefusalMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(**kwargs) -> ModelRefusalMiddleware:
    """Return the model refusal middleware."""
    return ModelRefusalMiddleware(**kwargs)
