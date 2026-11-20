"""Shared fixtures for the tests."""

# =========================================================================
# IMPORTS
# =========================================================================

import pytest

from agents_from_scratch.config.settings import settings


@pytest.fixture(scope="session")
def app_settings():
    """Return the application settings."""
    return settings
