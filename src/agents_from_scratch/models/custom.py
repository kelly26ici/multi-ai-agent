"""A custom chat model that replies with a fixed message."""

# =========================================================================
# IMPORTS
# =========================================================================

from collections.abc import Iterator
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatResult

# =========================================================================
# CUSTOM MODEL
# =========================================================================


class FixedChatModel(BaseChatModel):
    """Reply with the same message to every prompt."""

    reply: str = "I am a custom chat model."

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Return the fixed reply."""
        del messages, stop, run_manager, kwargs
        generation = ChatGeneration(message=AIMessage(content=self.reply))
        return ChatResult(generations=[generation])

    def _stream(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> Iterator[ChatGeneration]:
        """Yield the fixed reply in one chunk."""
        del messages, stop, run_manager, kwargs
        yield ChatGeneration(message=AIMessage(content=self.reply))

    @property
    def _llm_type(self) -> str:
        """Identify the model for LangChain."""
        return "fixed-chat-model"
