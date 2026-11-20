"""Delegate work to subagents that run their own tools."""

# =========================================================================
# IMPORTS
# =========================================================================

from deepagents.backends import FilesystemBackend
from deepagents.middleware import SubAgentMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(subagents: list[dict], **kwargs) -> SubAgentMiddleware:
    """Return the subagent middleware with a filesystem backend."""
    return SubAgentMiddleware(
        backend=FilesystemBackend(), subagents=subagents, **kwargs
    )
