"""Retriever backed by Redis."""

# =========================================================================
# GETTER
# =========================================================================


def get_retriever(embeddings, index_name: str, k: int = 4):
    """Return the Redis-backed retriever."""
    # TODO: Requires `uv add langchain-redis redis` and a running Redis.
    from langchain_redis import RedisVectorStore

    return RedisVectorStore(embeddings=embeddings, index_name=index_name).as_retriever(
        search_kwargs={"k": k}
    )
