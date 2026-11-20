"""Split text recursively on a list of separators."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter

# =========================================================================
# GETTER
# =========================================================================


def get_splitter(chunk_size: int = 400, chunk_overlap: int = 40):
    """Return the recursive character splitter."""
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
