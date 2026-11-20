"""The tools expose the response schemas the agents rely on."""

# =========================================================================
# IMPORTS
# =========================================================================

import pydantic
import pytest

from agents_from_scratch.config.prompts import MAIN_PROMPT
from agents_from_scratch.tools.base import get_tools
from agents_from_scratch.tools.calendar_tools import (
    ScheduleMeetingInput,
    check_calendar_availability,
    schedule_meeting,
)
from agents_from_scratch.tools.email_tools import WriteEmailInput, write_email


def test_get_tools_returns_the_default_set() -> None:
    """The registry lists every default tool by name."""
    assert [t.name for t in get_tools()] == [
        "write_email",
        "triage_email",
        "schedule_meeting",
        "check_calendar_availability",
        "Question",
        "Done",
    ]


def test_write_email_takes_one_pydantic_object() -> None:
    """The e-mail tool declares a single object argument."""
    assert list(write_email.args_schema.model_json_schema()["properties"]) == ["email"]
    assert set(WriteEmailInput.model_fields) == {"to", "subject", "content"}


def test_schedule_meeting_validates_the_input() -> None:
    """The calendar tool rejects empty attendees and out-of-range hours."""
    assert sorted(ScheduleMeetingInput.model_fields) == [
        "attendees",
        "duration_in_minutes",
        "preferred_day",
        "start_time",
        "subject",
    ]
    with pytest.raises(pydantic.ValidationError):
        ScheduleMeetingInput.model_validate(
            {
                "attendees": [],
                "subject": "s",
                "duration_in_minutes": 1,
                "preferred_day": "2026-11-20T10:00:00",
                "start_time": 9,
            }
        )
    with pytest.raises(pydantic.ValidationError):
        ScheduleMeetingInput.model_validate(
            {
                "attendees": ["a@b.com"],
                "subject": "s",
                "duration_in_minutes": 1,
                "preferred_day": "2026-11-20T10:00:00",
                "start_time": 99,
            }
        )


def test_triage_and_availability_are_named() -> None:
    """The remaining tools keep their names."""
    assert check_calendar_availability.name == "check_calendar_availability"
    assert schedule_meeting.name == "schedule_meeting"


def test_prompts_are_populated() -> None:
    """The main prompt is non-empty."""
    assert MAIN_PROMPT.strip()
