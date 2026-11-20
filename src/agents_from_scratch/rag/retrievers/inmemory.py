"""Retriever backed by a vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_retriever(vector_store, k: int = 4):
    """Return the top-k retriever for the vector store."""
    return vector_store.as_retriever(search_kwargs={"k": k})
