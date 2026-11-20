# =========================================================================
# IMPORTS
# =========================================================================

import base64
from email.mime.text import MIMEText
from typing import Literal

from googleapiclient.discovery import build
from langchain_core.tools import tool
from pydantic import BaseModel, EmailStr, Field

from agents_from_scratch.core.google import get_credentials

# =========================================================================
# EMAIL TOOLS
# =========================================================================


# -------------------------------------------------------------------------
# write_email
# -------------------------------------------------------------------------


class WriteEmailInput(BaseModel):
    """Input schema for write_email."""

    to: EmailStr = Field(description="The recipient of the e-mail.")
    subject: str = Field(description="The subject of the e-mail.")
    content: str = Field(description="The body of the e-mail.")


@tool
def write_email(email: WriteEmailInput) -> str:
    """Write and send an e-mail."""
    service = build("gmail", "v1", credentials=get_credentials())
    message = MIMEText(email.content)
    message["To"] = email.to
    message["Subject"] = email.subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    sent = service.users().messages().send(userId="me", body={"raw": raw}).execute()
    return f"E-mail sent to {email.to} with subject {email.subject}. Message id: {sent['id']}"


# -------------------------------------------------------------------------
# triage_email
# -------------------------------------------------------------------------


class TriageEmailInput(BaseModel):
    """Input schema for triage_email."""

    category: Literal["ignore", "notify", "respond"] = Field(
        description="The triage category to assign to the e-mail."
    )


@tool
def triage_email(triage: TriageEmailInput) -> str:
    """Triage an e-mail into one of three categories: ignore, notify, respond."""
    return f"Classification Decision: {triage.category}"


# -------------------------------------------------------------------------
# Done
# -------------------------------------------------------------------------


@tool
class Done(BaseModel):
    """E-mail has been sent."""

    done: bool = Field(description="Whether or not the e-mail has been sent.")


# -------------------------------------------------------------------------
# Question
# -------------------------------------------------------------------------


@tool
class Question(BaseModel):
    """Question to ask the user."""

    content: str = Field(description="The question to ask the user.")
