"""Chainlit chat UI for the e-mail assistant."""

# =========================================================================
# IMPORTS
# =========================================================================

import chainlit as cl
from langchain_core.messages import AIMessageChunk, HumanMessage
from langgraph.types import Command

from agents_from_scratch.agents.supervisor import agent
from agents_from_scratch.core.logger import logger

# =========================================================================
# SESSION
# =========================================================================


@cl.on_chat_start
async def on_chat_start() -> None:
    """Bind the supervisor to the chat thread."""
    cl.user_session.set(
        "config", {"configurable": {"thread_id": cl.context.session.id}}
    )


# =========================================================================
# MESSAGES
# =========================================================================


@cl.on_message
async def on_message(message: cl.Message) -> None:
    """Stream the supervisor's reply into the chat."""
    config = cl.user_session.get("config")
    answer = cl.Message(content="")

    async for chunk, _ in agent.astream(
        {"messages": [HumanMessage(message.content)]},
        config=config,
        stream_mode="messages",
    ):
        if isinstance(chunk, AIMessageChunk) and chunk.content:
            await answer.stream_token(chunk.content)

    await answer.send()
    await ask_for_review(config)


# =========================================================================
# HUMAN IN THE LOOP
# =========================================================================


async def ask_for_review(config: dict) -> None:
    """Ask for a decision when the graph is waiting on one."""
    state = await agent.aget_state(config)
    if not state.interrupts:
        return

    await cl.AskActionMessage(
        content=_pending_request(state.interrupts[0]),
        actions=[
            cl.Action(name="review", payload={"type": "approve"}, label="Approve"),
            cl.Action(name="review", payload={"type": "reject"}, label="Reject"),
        ],
    ).send()


def _pending_request(interrupt) -> str:
    """Describe the tool call that is waiting for the decision."""
    for action in interrupt.value.get("action_requests", []):
        if request := action.get("args", {}).get("request"):
            return f"The email writer is ready to run:\n\n> {request}\n\nApprove it?"
    return "The email writer is ready to run. Approve it?"


@cl.action_callback("review")
async def on_review(action: cl.Action) -> None:
    """Resume the paused run with the decision from the button payload."""
    await resume(action, {"decisions": [{"type": action.payload["type"]}]})


async def resume(action: cl.Action, decision: dict) -> None:
    """Continue the paused run and stream the final answer."""
    await action.remove()
    config = cl.user_session.get("config")
    answer = cl.Message(content="")

    try:
        async for chunk, _ in agent.astream(
            Command(resume=decision), config=config, stream_mode="messages"
        ):
            if isinstance(chunk, AIMessageChunk) and chunk.content:
                await answer.stream_token(chunk.content)
    except Exception as exc:  # noqa: BLE001
        logger.error("resume failed: %s", exc)
        await cl.Message(content=f"The run failed: {exc}").send()
        return

    await answer.send()
