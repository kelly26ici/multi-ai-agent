"""E-mail tools: write, triage, and the marker tools."""

# =========================================================================
# IMPORTS
# =========================================================================

from agents_from_scratch.tools.email.extras import Done, Question
from agents_from_scratch.tools.email.triage_email import (
    TriageEmailInput,
    triage_email,
)
from agents_from_scratch.tools.email.write_email import WriteEmailInput, write_email

# =========================================================================
# GROUP
# =========================================================================

email_tools = [write_email, triage_email, Question, Done]

__all__ = [
    "Done",
    "Question",
    "TriageEmailInput",
    "WriteEmailInput",
    "email_tools",
    "triage_email",
    "write_email",
]
