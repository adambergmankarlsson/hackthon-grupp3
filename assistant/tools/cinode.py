"""Cinode tool — fetches consultant profiles from Forefront's Cinode.

Reads profile markdown from `assistant/profiles/`. To make it a real integration,
replace the file read in `fetch_cinode_profile` with a Cinode API call — the
function signature and the roster stay the same.
"""

import pathlib

_PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def load_cinode_roster() -> str:
    """Return the Cinode roster (people + ids) for the agent's context."""
    return (_PROFILES_DIR / "roster.md").read_text(encoding="utf-8")


def fetch_cinode_profile(cinode_id: str) -> dict:
    """Fetch a consultant's full Cinode profile by id.

    Use this to look up a person's background, skills, certifications and past
    assignments — either the current user or someone they ask about. Pick the
    `cinode_id` from the Cinode roster in your instructions.

    Args:
        cinode_id: A roster id, e.g. "adam", "patrik", "tove", "mikaela", "anna".

    Returns:
        On success: {"status": "ok", "cinode_id": ..., "profile": <profile text>}.
        On failure: {"status": "error", "error_message": ..., "available_profiles": [...]}.
    """
    available = sorted(p.stem for p in _PROFILES_DIR.glob("*.md") if p.stem != "roster")
    profile_path = _PROFILES_DIR / f"{cinode_id.lower()}.md"
    if cinode_id.lower() == "roster" or not profile_path.exists():
        return {
            "status": "error",
            "error_message": f"Unknown cinode_id {cinode_id!r}.",
            "available_profiles": available,
        }
    return {
        "status": "ok",
        "cinode_id": cinode_id.lower(),
        "profile": profile_path.read_text(encoding="utf-8"),
    }
