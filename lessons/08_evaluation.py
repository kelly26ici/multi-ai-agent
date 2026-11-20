"""Evaluation: score a target function against labelled examples."""

# =========================================================================
# IMPORTS
# =========================================================================

from langsmith import evaluate

from agents_from_scratch.core.logger import logger

# =========================================================================
# TARGET
# =========================================================================


def echo(inputs: dict) -> dict:
    """Return the echo of the question."""
    return {"answer": inputs["question"] + "!"}


# =========================================================================
# EXAMPLES
# =========================================================================

examples = [
    {"inputs": {"question": "hi"}, "outputs": {"answer": "hi!"}},
    {"inputs": {"question": "bye"}, "outputs": {"answer": "bye!"}},
]


# =========================================================================
# EVALUATORS
# =========================================================================


def exact_match(outputs: dict, reference_outputs: dict) -> bool:
    """Check the output equals the gold answer."""
    return outputs["answer"] == reference_outputs["answer"]


if __name__ == "__main__":
    logger.info("Running the evaluation")
    evaluate(echo, data=examples, evaluators=[exact_match])
