"""Google OAuth credentials for the Gmail and Calendar tools."""

# =========================================================================
# IMPORTS
# =========================================================================

import json
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from agents_from_scratch.core.logger import logger

# =========================================================================
# GOOGLE CREDENTIALS
# =========================================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar.events",
]
SECRETS_DIR = Path(".secrets")
CREDENTIALS_PATH = SECRETS_DIR / "credentials.json"
TOKEN_PATH = SECRETS_DIR / "token.json"
TOKEN_ENV_VAR = "GOOGLE_TOKEN_JSON"

_MISSING_TOKEN = (
    "No Google OAuth token configured. Set GOOGLE_TOKEN_JSON to the contents "
    "of a token.json authorized with the gmail.send and calendar.events "
    "scopes, or run the consent flow locally to write .secrets/token.json."
)
_MISSING_REFRESH = (
    "The Google OAuth token has no refresh token. Re-run the consent flow "
    "locally and store the new token in GOOGLE_TOKEN_JSON."
)


class MissingCredentialsError(RuntimeError):
    """No usable Google OAuth token is available."""


def _from_env() -> Credentials | None:
    """Build credentials from the GOOGLE_TOKEN_JSON env var, if set."""
    if not (raw := os.getenv(TOKEN_ENV_VAR)):
        return None
    return Credentials.from_authorized_user_info(json.loads(raw), SCOPES)


def _from_file() -> Credentials | None:
    """Build credentials from the saved token file, if it exists."""
    if not TOKEN_PATH.exists():
        return None
    return Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)


def _consent() -> Credentials:
    """Run the browser consent flow for first-time local setup."""
    if not CREDENTIALS_PATH.exists():
        raise MissingCredentialsError(_MISSING_TOKEN)
    logger.info("Opening the browser for Google OAuth consent")
    SECRETS_DIR.mkdir(exist_ok=True)
    creds = InstalledAppFlow.from_client_secrets_file(
        str(CREDENTIALS_PATH), SCOPES
    ).run_local_server(port=0)
    TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
    return creds


def get_credentials() -> Credentials:
    """Return OAuth credentials, preferring the env var over the saved file.

    An expired token refreshes in place. With nothing configured the error
    says how to provide a token instead of failing deep inside a tool call.
    """
    creds, from_env = None, False
    if (env_creds := _from_env()) is not None:
        creds, from_env = env_creds, True
    elif (file_creds := _from_file()) is not None:
        creds = file_creds
    else:
        return _consent()

    if creds.valid:
        return creds
    if creds.expired and creds.refresh_token:
        logger.info("Refreshing the Google OAuth token")
        creds.refresh(Request())
        if not from_env:
            TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        return creds
    if creds.refresh_token is None:
        raise MissingCredentialsError(_MISSING_REFRESH)
    raise MissingCredentialsError(_MISSING_TOKEN)
