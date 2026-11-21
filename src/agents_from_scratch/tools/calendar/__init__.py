"""Calendar tools: schedule and check availability."""

# =========================================================================
# IMPORTS
# =========================================================================

from agents_from_scratch.tools.calendar.check_calendar_availability import (
    CheckCalendarAvailabilityInput,
    check_calendar_availability,
)
from agents_from_scratch.tools.calendar.schedule_meeting import (
    ScheduleMeetingInput,
    schedule_meeting,
)

# =========================================================================
# GROUP
# =========================================================================

calendar_tools = [schedule_meeting, check_calendar_availability]

__all__ = [
    "CheckCalendarAvailabilityInput",
    "ScheduleMeetingInput",
    "calendar_tools",
    "check_calendar_availability",
    "schedule_meeting",
]
