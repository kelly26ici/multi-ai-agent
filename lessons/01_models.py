"""Chat models: init, messages, and the two ways to configure them."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.chat_models import init_chat_model
from langchain.messages import AIMessage, HumanMessage
from langchain_core.messages import BaseMessage

from agents_from_scratch.config.settings import settings
from agents_from_scratch.core.logger import logger

# =========================================================================
# FIXED MODEL
# =========================================================================

model = init_chat_model(
    settings.default_model,
    temperature=settings.temperature,
    api_key=settings.nvidia_api_key.get_secret_value(),
)


# =========================================================================
# CONFIGURABLE MODEL
# =========================================================================

configurable = init_chat_model(
    "nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
    temperature=0,
    configurable_fields="any",
    api_key=settings.nvidia_api_key.get_secret_value(),
)


# =========================================================================
# MESSAGES
# =========================================================================

messages: list[BaseMessage] = [
    HumanMessage("What is an agent?", name="rex"),
    AIMessage("A loop of model, tools, and decisions."),
    HumanMessage("Show me one."),
]


if __name__ == "__main__":
    logger.info("Invoking the fixed model")
    logger.info(model.invoke(messages).content)

    logger.info("Invoking the configurable model")
    logger.info(
        configurable.invoke(messages, config={"model": settings.default_model}).content
    )

    logger.info("Streaming tokens")
    for chunk in model.stream("Say hello in five words."):
        logger.info(chunk.content)
