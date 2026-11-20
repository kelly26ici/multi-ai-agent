"""Milvus vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(
    embeddings, collection_name: str = "agents_from_scratch", **kwargs
):
    """Return the Milvus vector store."""
    # TODO: Requires `uv add langchain-milvus pymilvus` and a running Milvus.
    from langchain_milvus import Milvus

    return Milvus(
        embedding_function=embeddings,
        collection_name=collection_name,
        **kwargs,
    )
