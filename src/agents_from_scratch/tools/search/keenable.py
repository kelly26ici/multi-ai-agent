"""Search the web with Keenable."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_keenable import KeenableSearch

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Keenable search tool."""
    return KeenableSearch(api_key=settings.keenable_api_key.get_secret_value())
