"""The tools expose the response schemas the agents rely on."""

# =========================================================================
# IMPORTS
# =========================================================================

import pydantic
import pytest

from agents_from_scratch.config.prompts import SUPERVISOR_PROMPT
from agents_from_scratch.tools import (
    calendar_tools,
    crawl_tools,
    email_tools,
    get_all_tools,
)
from agents_from_scratch.tools.calendar import ScheduleMeetingInput
from agents_from_scratch.tools.email import WriteEmailInput
from agents_from_scratch.tools.email.write_email import write_email
from agents_from_scratch.tools.search import get_search_tools


def test_email_group_holds_the_four_tools() -> None:
    """The e-mail group lists its tools by name."""
    assert [t.name for t in email_tools] == [
        "write_email",
        "triage_email",
        "Question",
        "Done",
    ]


def test_calendar_group_holds_the_two_tools() -> None:
    """The calendar group lists its tools by name."""
    assert [t.name for t in calendar_tools] == [
        "schedule_meeting",
        "check_calendar_availability",
    ]


def test_get_all_tools_merges_every_group() -> None:
    """The all-tools option is the union of the groups."""
    search = get_search_tools()
    all_names = [t.name for t in get_all_tools()]
    assert set(all_names) == {
        t.name for t in [*email_tools, *calendar_tools, *crawl_tools, *search]
    }
    assert len(all_names) == (
        len(email_tools) + len(calendar_tools) + len(crawl_tools) + len(search)
    )


def test_write_email_takes_one_pydantic_object() -> None:
    """The e-mail tool declares a single object argument."""
    assert list(write_email.args_schema.model_json_schema()["properties"]) == ["email"]
    assert set(WriteEmailInput.model_fields) == {"to", "subject", "content"}


def test_schedule_meeting_validates_the_input() -> None:
    """The calendar tool rejects empty attendees and out-of-range hours."""
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


def test_search_tools_take_a_query_object() -> None:
    """Every search tool declares a query argument."""
    for tool_item in get_search_tools():
        properties = tool_item.args_schema.model_json_schema()["properties"]
        assert "query" in properties, tool_item.name


def test_supervisor_prompt_is_populated() -> None:
    """The supervisor prompt is non-empty."""
    assert SUPERVISOR_PROMPT.strip()
