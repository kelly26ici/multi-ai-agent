"""Search the web with Exa."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_exa import ExaSearchResults

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Exa search tool."""
    return ExaSearchResults(api_key=settings.exa_api_key.get_secret_value())
