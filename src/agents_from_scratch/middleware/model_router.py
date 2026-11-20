"""Route each run to a model chosen by a decision model."""

# =========================================================================
# IMPORTS
# =========================================================================

from langchain.agents.middleware import ModelChoice, ModelRouterMiddleware

# =========================================================================
# GETTER
# =========================================================================


def get_middleware(
    choices: dict, instructions: str, classifier
) -> ModelRouterMiddleware:
    """Return the model router middleware."""
    return ModelRouterMiddleware(
        choices=choices,
        instructions=instructions,
        classifier=classifier,
    )


# =========================================================================
# EXAMPLES
# =========================================================================

DEFAULT_CHOICE = ModelChoice(
    model="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
    criteria="General chat and tool calls.",
)


ROUTER_INSTRUCTIONS = (
    "Pick the choice that matches the task. Answer with the choice label."
)
