"""Memory: a key-value store survives across threads and runs."""

# =========================================================================
# IMPORTS
# =========================================================================

from langgraph.store.memory import InMemoryStore

from agents_from_scratch.core.logger import logger

# =========================================================================
# STORE
# =========================================================================

store = InMemoryStore()


# =========================================================================
# PUT AND GET
# =========================================================================

store.put(("users", "rex"), "profile", {"language": "en", "tone": "concise"})
profile = store.get(("users", "rex"), "profile")


# =========================================================================
# SEARCH
# =========================================================================

items = list(store.search(("users", "rex")))


if __name__ == "__main__":
    logger.info("Reading back the stored profile")
    logger.info(profile.value)

    logger.info("Searching the namespace")
    for item in items:
        logger.info(item.key)
