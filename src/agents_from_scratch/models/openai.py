"""OpenAI chat model."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.chat_models import init_chat_model

# =========================================================================
# GETTER
# =========================================================================


def get_model(model: str, **kwargs):
    """Return the OpenAI chat model."""
    return init_chat_model(f"openai:{model}", **kwargs)
