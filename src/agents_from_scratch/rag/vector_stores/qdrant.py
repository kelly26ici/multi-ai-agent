"""Qdrant vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(
    embeddings, collection_name: str = "agents-from-scratch", **kwargs
):
    """Return the Qdrant vector store."""
    # TODO: Requires `uv add langchain-qdrant qdrant-client`.
    from langchain_qdrant import QdrantVectorStore

    return QdrantVectorStore.from_texts(
        texts=[], embedding=embeddings, collection_name=collection_name, **kwargs
    )
