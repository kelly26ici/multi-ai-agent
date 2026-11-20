"""Registry of the tools the assistant can use."""

# =========================================================================
# IMPORTS
# =========================================================================

from agents_from_scratch.tools.calendar_tools import (
    check_calendar_availability,
    schedule_meeting,
)
from agents_from_scratch.tools.email_tools import (
    Done,
    Question,
    triage_email,
    write_email,
)

# =========================================================================
# REGISTRY
# =========================================================================


def get_tools() -> list:
    """Return every default tool for the assistant."""
    return [
        write_email,
        triage_email,
        schedule_meeting,
        check_calendar_availability,
        Question,
        Done,
    ]
