"""OpenAI embeddings."""

# =========================================================================
# GETTER
# =========================================================================


def get_embeddings(**kwargs):
    """Return the OpenAI embedding model."""
    # TODO: Requires `uv add langchain-openai`.
    from langchain_openai import OpenAIEmbeddings

    return OpenAIEmbeddings(**kwargs)
