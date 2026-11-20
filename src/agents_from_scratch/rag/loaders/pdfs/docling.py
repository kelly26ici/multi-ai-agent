"""Load a PDF into documents with Docling."""

# =========================================================================
# GETTER
# =========================================================================


def get_loader(path):
    """Return the Docling PDF loader."""
    # TODO: Requires `uv add langchain-docling docling`.
    from langchain_docling import DoclingLoader

    return DoclingLoader(file_path=path)
