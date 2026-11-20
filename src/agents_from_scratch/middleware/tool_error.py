"""Send tool errors back to the model as ToolMessages."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ToolErrorMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(**kwargs) -> ToolErrorMiddleware:
    """Return the tool error middleware."""
    return ToolErrorMiddleware(**kwargs)
