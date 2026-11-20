"""Chroma vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(
    embeddings, collection_name: str = "agents-from-scratch", **kwargs
):
    """Return the Chroma vector store."""
    # TODO: Requires `uv add langchain-chroma`.
    from langchain_chroma import Chroma

    return Chroma(
        embedding_function=embeddings,
        collection_name=collection_name,
        **kwargs,
    )
