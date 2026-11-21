"""Schedule a meeting on the primary calendar."""

# =========================================================================
# IMPORTS
# =========================================================================

from datetime import UTC, datetime, timedelta

from googleapiclient.discovery import build
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from agents_from_scratch.core.google import get_credentials

# -------------------------------------------------------------------------
# schedule_meeting
# -------------------------------------------------------------------------


class ScheduleMeetingInput(BaseModel):
    """Input schema for schedule_meeting."""

    attendees: list[str] = Field(
        min_length=1, description="E-mail addresses of the meeting attendees."
    )
    subject: str = Field(
        min_length=1, description="The subject or title of the meeting."
    )
    duration_in_minutes: int = Field(gt=0, description="Meeting duration in minutes.")
    preferred_day: datetime = Field(description="Preferred meeting date.")
    start_time: int = Field(
        ge=0, le=23, description="Meeting start hour in 24-hour format (0-23)."
    )


@tool
def schedule_meeting(meeting: ScheduleMeetingInput) -> str:
    """Schedule a calendar meeting."""
    start = meeting.preferred_day.replace(
        hour=meeting.start_time, minute=0, second=0, microsecond=0, tzinfo=UTC
    )
    end = start + timedelta(minutes=meeting.duration_in_minutes)
    service = build("calendar", "v3", credentials=get_credentials())
    created = (
        service.events()
        .insert(
            calendarId="primary",
            body={
                "summary": meeting.subject,
                "start": {"dateTime": start.isoformat()},
                "end": {"dateTime": end.isoformat()},
                "attendees": [{"email": attendee} for attendee in meeting.attendees],
            },
        )
        .execute()
    )
    date_str = start.strftime("%A, %B %d, %Y")
    time_str = start.strftime("%I:%M %p")
    return f"Meeting '{meeting.subject}' scheduled on {date_str} at {time_str} UTC for {meeting.duration_in_minutes} minutes with {len(meeting.attendees)} attendees. Event id: {created['id']}"
