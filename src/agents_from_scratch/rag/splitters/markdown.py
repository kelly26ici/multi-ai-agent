"""Split markdown on its headers."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_text_splitters import MarkdownHeaderTextSplitter

# =========================================================================
# GETTER
# =========================================================================


def get_splitter():
    """Return the markdown header splitter."""
    return MarkdownHeaderTextSplitter()
