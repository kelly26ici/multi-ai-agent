"""Split text where the meaning changes."""

# =========================================================================
# GETTER
# =========================================================================


def get_splitter(embeddings, breakpoint_threshold_type: str = "percentile"):
    """Return the semantic chunker for the given embeddings."""
    # TODO: Requires `uv add langchain-experimental`.
    from langchain_experimental.text_splitter import SemanticChunker

    return SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type=breakpoint_threshold_type,
    )
