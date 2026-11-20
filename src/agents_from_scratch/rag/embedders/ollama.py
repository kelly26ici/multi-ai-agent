"""Ollama embeddings."""

# =========================================================================
# GETTER
# =========================================================================


def get_embeddings(**kwargs):
    """Return the local Ollama embedding model."""
    # TODO: Requires `uv add langchain-ollama` and a running Ollama server.
    from langchain_ollama import OllamaEmbeddings

    return OllamaEmbeddings(**kwargs)
