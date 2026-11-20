# =========================================================================
# IMPORTS
# =========================================================================

import httpx

# =========================================================================
# HTTP CLIENT
# =========================================================================

client = httpx.AsyncClient(
    timeout=httpx.Timeout(30.0),
    follow_redirects=True,
    headers={"User-Agent": "agents-from-scratch/0.1"},
)


async def close_client() -> None:
    """Close the shared HTTP client on app shutdown."""
    await client.aclose()
