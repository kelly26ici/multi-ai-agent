"""Search the web with Linkup."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_linkup import LinkupSearchTool

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Linkup search tool, keyed from LINKUP_API_KEY."""
    return LinkupSearchTool(depth="standard")
