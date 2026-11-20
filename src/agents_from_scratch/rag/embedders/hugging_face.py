"""Hugging Face embeddings."""

# =========================================================================
# GETTER
# =========================================================================


def get_embeddings(**kwargs):
    """Return the Hugging Face embedding model."""
    # TODO: Requires `uv add langchain-huggingface`.
    from langchain_huggingface import HuggingFaceEmbeddings

    return HuggingFaceEmbeddings(**kwargs)
