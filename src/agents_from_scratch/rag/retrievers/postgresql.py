"""Retriever backed by PGVector."""

# =========================================================================
# GETTER
# =========================================================================


def get_retriever(embeddings, connection: str, k: int = 4):
    """Return the Postgres-backed retriever."""
    # TODO: Requires `uv add langchain-postgres` and a running Postgres with pgvector.
    from langchain_postgres import PGVector

    return PGVector(embeddings=embeddings, connection=connection).as_retriever(
        search_kwargs={"k": k}
    )
