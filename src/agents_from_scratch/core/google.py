# =========================================================================
# IMPORTS
# =========================================================================

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


def get_credentials() -> Credentials:
    """Return saved OAuth credentials, refreshing or re-consenting as needed."""
    SECRETS_DIR.mkdir(exist_ok=True)
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info("Refreshing the Google OAuth token")
            creds.refresh(Request())
        else:
            logger.info("Opening the browser for Google OAuth consent")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES
            )
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json())
    return creds
