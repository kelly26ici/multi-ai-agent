"""NVIDIA embeddings."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

from agents_from_scratch.config.settings import settings

# =========================================================================
# GETTER
# =========================================================================


def get_embeddings(**kwargs) -> NVIDIAEmbeddings:
    """Return the NVIDIA embedding model."""
    return NVIDIAEmbeddings(
        api_key=settings.nvidia_api_key.get_secret_value(), **kwargs
    )
