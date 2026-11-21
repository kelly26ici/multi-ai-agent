# =========================================================================
# IMPORTS
# =========================================================================
import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build
from langchain_core.tools import tool
from pydantic import BaseModel, EmailStr, Field

from agents_from_scratch.core.google import get_credentials

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
