"""RAG: load, split, embed, store, and retrieve."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# DOCUMENTS
# =========================================================================

documents = [
    Document(
        page_content=(
            "An agent runs a loop: the model is called, tools may be chosen, "
            "and results feed back into the next model call until a stopping "
            "condition is met. Tools are just functions with schemas."
        ),
        metadata={"source": "agents-docs"},
    ),
    Document(
        page_content=(
            "Retrieval-augmented generation grounds answers in your own text "
            "by embedding chunks and fetching the relevant ones at query time."
        ),
        metadata={"source": "rag-docs"},
    ),
]


# =========================================================================
# PIPELINE
# =========================================================================


def run() -> list[str]:
    """Split, embed, store, and retrieve the documents."""
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=20
    ).split_documents(documents)
    store = InMemoryVectorStore.from_documents(
        chunks, NVIDIAEmbeddings(api_key=settings.nvidia_api_key.get_secret_value())
    )
    return [
        doc.page_content
        for doc in store.similarity_search("How does an agent decide?", k=2)
    ]


if __name__ == "__main__":
    logger.info("Retrieving for the query")
    for hit in run():
        logger.info(hit)
