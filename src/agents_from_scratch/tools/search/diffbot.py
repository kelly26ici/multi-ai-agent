"""Search the web with Diffbot."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_diffbot import DiffbotWebSearchTool

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_tool():
    """Return the Diffbot web search tool."""
    return DiffbotWebSearchTool(api_key=settings.diffbot_api_key.get_secret_value())
