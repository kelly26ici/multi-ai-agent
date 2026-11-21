"""Google OAuth credentials come from the env var, the file, or fail loudly."""

# =========================================================================
# IMPORTS
# =========================================================================

import json

import pytest
from google.oauth2.credentials import Credentials

from agents_from_scratch.core import google
from agents_from_scratch.core.google import MissingCredentialsError, get_credentials

# =========================================================================
# TESTS
# =========================================================================


def _token_dict() -> dict:
    """A token payload shaped like Google's token.json."""
    return {
        "token": "access-token",
        "refresh_token": "refresh-token",
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": "client-id",
        "client_secret": "client-secret",
        "scopes": google.SCOPES,
        "expiry": "2027-01-01T00:00:00Z",
    }


def test_env_token_builds_credentials(monkeypatch) -> None:
    """GOOGLE_TOKEN_JSON is used when set."""
    monkeypatch.setenv("GOOGLE_TOKEN_JSON", json.dumps(_token_dict()))
    creds = get_credentials()
    assert isinstance(creds, Credentials)
    assert creds.refresh_token == "refresh-token"


def test_file_token_builds_credentials(tmp_path, monkeypatch) -> None:
    """The saved token file is used when no env var is set."""
    token = tmp_path / "token.json"
    token.write_text(json.dumps(_token_dict()), encoding="utf-8")
    monkeypatch.delenv("GOOGLE_TOKEN_JSON", raising=False)
    monkeypatch.setattr(google, "TOKEN_PATH", token)
    creds = get_credentials()
    assert creds.refresh_token == "refresh-token"


def test_no_token_raises_a_clear_error(tmp_path, monkeypatch) -> None:
    """No configured token raises instead of failing deep in a tool."""
    monkeypatch.delenv("GOOGLE_TOKEN_JSON", raising=False)
    monkeypatch.setattr(google, "TOKEN_PATH", tmp_path / "missing-token.json")
    monkeypatch.setattr(google, "CREDENTIALS_PATH", tmp_path / "missing-client.json")
    with pytest.raises(MissingCredentialsError):
        get_credentials()
