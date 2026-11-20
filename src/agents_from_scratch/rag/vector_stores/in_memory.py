"""In-memory vector store."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_core.vectorstores import InMemoryVectorStore

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(embeddings) -> InMemoryVectorStore:
    """Return the in-memory vector store for the embeddings."""
    return InMemoryVectorStore(embeddings)
