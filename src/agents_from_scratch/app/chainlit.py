"""Chainlit chat UI for the e-mail assistant."""

# =========================================================================
# IMPORTS
# =========================================================================

import chainlit as cl
from langchain_core.messages import AIMessageChunk, HumanMessage
from langgraph.types import Command

from agents_from_scratch.agents.supervisor import agent

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
    """Ask for a decision when the graph paused on the email writer."""
    state = await agent.aget_state(config)
    if not state.next:
        return

    await cl.AskActionMessage(
        content="The email writer is ready to run. Approve it?",
        actions=[
            cl.Action(name="approve", value="approve", label="Approve"),
            cl.Action(name="reject", value="reject", label="Reject"),
        ],
    ).send()


@cl.action_callback("approve")
async def on_approve(action: cl.Action) -> None:
    """Resume the paused run with the approval."""
    await resume(action, {"decisions": [{"type": "approve"}]})


@cl.action_callback("reject")
async def on_reject(action: cl.Action) -> None:
    """Resume the paused run with the rejection."""
    await resume(action, {"decisions": [{"type": "reject"}]})


async def resume(action: cl.Action, decision: dict) -> None:
    """Continue the paused run and stream the final answer."""
    await action.remove()
    config = cl.user_session.get("config")
    answer = cl.Message(content="")

    async for chunk, _ in agent.astream(
        Command(resume=decision), config=config, stream_mode="messages"
    ):
        if isinstance(chunk, AIMessageChunk) and chunk.content:
            await answer.stream_token(chunk.content)

    await answer.send()
