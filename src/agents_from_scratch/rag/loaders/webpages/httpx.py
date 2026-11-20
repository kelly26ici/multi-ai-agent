"""Load a web page into a document with the shared HTTP client."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_core.documents import Document

from agents_from_scratch.core.clients import client

# =========================================================================
# LOADER
# =========================================================================


async def load(url: str) -> Document:
    """Fetch the page and return it as one document."""
    response = await client.get(url)
    response.raise_for_status()
    return Document(page_content=response.text, metadata={"source": url})
