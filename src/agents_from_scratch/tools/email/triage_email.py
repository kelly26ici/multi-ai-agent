"""Triage an incoming e-mail."""

# =========================================================================
# IMPORTS
# =========================================================================

from typing import Literal

from langchain_core.tools import tool
from pydantic import BaseModel, Field

# =========================================================================
# TOOL
# =========================================================================


class TriageEmailInput(BaseModel):
    """Input schema for triage_email."""

    category: Literal["ignore", "notify", "respond"] = Field(
        description="The triage category to assign to the e-mail."
    )


@tool
def triage_email(triage: TriageEmailInput) -> str:
    """Triage an e-mail into one of three categories: ignore, notify, respond."""
    return f"Classification Decision: {triage.category}"
