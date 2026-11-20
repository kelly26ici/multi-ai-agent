"""Load a PDF into documents with PyMuPDF."""

# =========================================================================
# IMPORTS
# =========================================================================

from pathlib import Path

from langchain_core.documents import Document

# =========================================================================
# LOADER
# =========================================================================


def load(path: Path) -> list[Document]:
    """Return one document per PDF page with the page text."""
    # TODO: Requires `uv add pymupdf`.
    import fitz

    with fitz.open(path) as pdf:
        return [
            Document(page_content=page.get_text(), metadata={"page": number})
            for number, page in enumerate(pdf)
        ]
