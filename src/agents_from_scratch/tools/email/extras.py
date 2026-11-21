"""Marker tools the agents use to hand control back."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain_core.tools import tool
from pydantic import BaseModel, Field

# =========================================================================
# TOOLS
# =========================================================================


@tool
class Done(BaseModel):
    """E-mail has been sent."""

    done: bool = Field(description="Whether or not the e-mail has been sent.")


@tool
class Question(BaseModel):
    """Question to ask the user."""

    content: str = Field(description="The question to ask the user.")
