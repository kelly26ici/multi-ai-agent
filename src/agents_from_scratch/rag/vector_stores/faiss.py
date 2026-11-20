"""FAISS vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(embeddings, **kwargs):
    """Return the FAISS vector store."""
    # TODO: Requires `uv add faiss-cpu langchain-community`.
    from langchain_community.vectorstores import FAISS

    return FAISS(embedding_function=embeddings, **kwargs)
