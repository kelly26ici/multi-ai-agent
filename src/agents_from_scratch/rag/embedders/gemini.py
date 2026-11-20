"""Gemini embeddings."""

# =========================================================================
# GETTER
# =========================================================================


def get_embeddings(**kwargs):
    """Return the Google Gemini embedding model."""
    # TODO: Requires `uv add langchain-google-genai`.
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    return GoogleGenerativeAIEmbeddings(**kwargs)
