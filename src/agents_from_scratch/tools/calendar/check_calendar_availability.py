"""Check what the primary calendar holds for one day."""

# =========================================================================
# IMPORTS
# =========================================================================

from datetime import UTC, date, datetime, time

from googleapiclient.discovery import build
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.core.google import get_credentials

# =========================================================================
# TOOL
# =========================================================================


class CheckCalendarAvailabilityInput(BaseModel):
    """Input schema for check_calendar_availability."""

    day: date = Field(description="The date to check for available meeting slots.")


@tool
def check_calendar_availability(
    availability: CheckCalendarAvailabilityInput,
) -> str:
    """Check the calendar availability for a given day."""
    day = availability.day
    service = build("calendar", "v3", credentials=get_credentials())
    events = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=datetime.combine(day, time.min, tzinfo=UTC).isoformat(),
            timeMax=datetime.combine(day, time.max, tzinfo=UTC).isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
        .get("items", [])
    )
    day_str = day.strftime("%A, %B %d, %Y")
    if not events:
        return f"No events scheduled on {day_str}."
    busy = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        busy.append(f"{start} - {end}: {event['summary']}")
    return f"Busy on {day_str}: " + "; ".join(busy)
