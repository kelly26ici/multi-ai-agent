"""Fall back to other models when the primary fails."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ModelFallbackMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(*fallback_models: str, **kwargs) -> ModelFallbackMiddleware:
    """Return the model fallback middleware."""
    return ModelFallbackMiddleware(fallback_models=list(fallback_models), **kwargs)
