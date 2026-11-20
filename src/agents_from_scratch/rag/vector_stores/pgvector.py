"""PGVector vector store."""

# =========================================================================
# GETTER
# =========================================================================


def get_vector_store(embeddings, connection: str, **kwargs):
    """Return the PGVector store for the connection string."""
    # TODO: Requires `uv add langchain-postgres` and a running Postgres with pgvector.
    from langchain_postgres import PGVector

    return PGVector(embeddings=embeddings, connection=connection, **kwargs)
