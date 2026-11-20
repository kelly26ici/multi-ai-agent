"""Run the whole test suite from the command line."""

# =========================================================================
# IMPORTS
# =========================================================================

import sys

import pytest


def main() -> None:
    """Run pytest over the tests directory."""
    raise SystemExit(pytest.main(["-q", *sys.argv[1:]]))


if __name__ == "__main__":
    main()
