"""Tool prompt templates for the e-mail assistant."""


# =========================================================================
# STANDARD TOOLS
# =========================================================================

STANDARD_TOOL_PROMPT = """
1. triage_email(ignore, notify, respond) - Triage an e-mail into one of three categories.
2. write_email() - Write and send an e-mail.
3. schedule_meeting() - Schedule a calendar meeting.
4. check_calendar_availability() - Check the calendar availability for a given day.
5. Done() - Call when the e-mail has been handled.
"""


# =========================================================================
# HUMAN-IN-THE-LOOP TOOLS
# =========================================================================

HITL_TOOLS_PROMPT = """
1. write_email() - Write and send an e-mail.
2. schedule_meeting() - Schedule a calendar meeting.
3. check_calendar_availability() - Check the calendar availability for a given day.
4. Question() - Ask the user a clarifying question.
5. Done() - Call when the user's request has been handled.
"""


# =========================================================================
# HUMAN-IN-THE-LOOP TOOLS WITH MEMORY
# =========================================================================

# TODO: Implement the manage_memory tool once the memory module is written.

HITL_MEMORY_TOOLS_PROMPT = """
1. write_email() - Write and send an e-mail.
2. schedule_meeting() - Schedule a calendar meeting.
3. check_calendar_availability() - Check the calendar availability for a given day.
4. manage_memory() - Store or update the user's preferences and instructions.
5. Question() - Ask the user a clarifying question.
6. Done() - Call when the user's request has been handled.
"""


# =========================================================================
# AGENT TOOLS
# =========================================================================

AGENT_TOOLS_PROMPT = """
1. write_email() - Write and send an e-mail.
2. schedule_meeting() - Schedule a calendar meeting.
3. check_calendar_availability() - Check the calendar availability for a given day.
4. Question() - Ask the user a clarifying question.
5. Done() - Call when the user's request has been handled.
"""
