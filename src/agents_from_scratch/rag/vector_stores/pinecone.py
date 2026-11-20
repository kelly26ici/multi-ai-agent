"""Pinecone vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(embeddings, index_name: str, **kwargs):
    """Return the Pinecone vector store for the index."""
    # TODO: Requires `uv add langchain-pinecone` and a Pinecone API key.
    from langchain_pinecone import PineconeVectorStore

    return PineconeVectorStore(embedding=embeddings, index_name=index_name, **kwargs)
