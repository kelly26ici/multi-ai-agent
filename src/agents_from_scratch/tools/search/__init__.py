"""Search tools, one getter per provider, gathered for the researcher."""

# =========================================================================
# IMPORTS
# =========================================================================

from loguru import logger

from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.search import (
    agent_search,
    cloro,
    crustapi,
    diffbot,
    exa,
    firecrawl,
    keenable,
    linkup,
    querit,
    serpapi,
    tavily,
)

# =========================================================================
# PROVIDER TABLES
# =========================================================================

KEYED = {
    "tavily": (tavily.get_tool, settings.tavily_api_key),
    "exa": (exa.get_tool, settings.exa_api_key),
    "keenable": (keenable.get_tool, settings.keenable_api_key),
    "diffbot": (diffbot.get_tool, settings.diffbot_api_key),
    "linkup": (linkup.get_tool, settings.linkup_api_key),
    "firecrawl": (firecrawl.get_tool, settings.firecrawl_api_key),
    "serpapi": (serpapi.get_tool, settings.serpapi_api_key),
    "querit": (querit.get_tool, settings.querit_api_key),
    "crustapi": (crustapi.get_tool, settings.crustapi_api_key),
    "cloro": (cloro.get_tool, settings.cloro_api_key),
}

KEYLESS = {
    "agent_search": agent_search.get_tool,
}


# =========================================================================
# GROUP
# =========================================================================


def get_search_tools() -> list:
    """Return the keyless search tools plus the keyed ones with keys set."""
    tools = [getter() for getter in KEYLESS.values()]
    for name, (getter, key) in KEYED.items():
        if key is None:
            logger.warning(f"{name}_api_key is not set; skipping its search tool")
            continue
        tools.append(getter())
    return tools
