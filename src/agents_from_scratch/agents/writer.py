"""Agent that drafts e-mail replies."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from agents_from_scratch.config.prompts import WRITER_PROMPT
from agents_from_scratch.config.settings import settings
from agents_from_scratch.tools.email_tools import write_email

# =========================================================================
# AGENT
# =========================================================================

agent = create_agent(
    init_chat_model(
        settings.default_model,
        api_key=settings.nvidia_api_key.get_secret_value(),
    ),
    tools=[write_email],
    system_prompt=WRITER_PROMPT,
)
