"""Workvivo feed tool — a mockup of Forefront's internal company feed.

Today this reads exported PDFs from `assistant/workvivo_feed/`. To make it a real
integration, replace the PDF read in `fetch_workvivo_post` with a Workvivo API
call — the function signature and the catalog stay the same.
"""

import pathlib

import pypdf

_FEED_DIR = pathlib.Path(__file__).resolve().parent.parent / "workvivo_feed"


def load_workvivo_catalog() -> str:
    """Return the Workvivo catalog (one entry per space) for the agent's context."""
    return (_FEED_DIR / "catalog.md").read_text(encoding="utf-8")


def fetch_workvivo_post(space_id: str) -> dict:
    """Fetch the full text of internal Workvivo feed posts for a given space.

    Use this to ground answers in Forefront's internal company feed. Pick the
    `space_id` from the Workvivo catalog in your instructions based on what the
    user is asking about.

    Args:
        space_id: A catalog space id, e.g. "genai-agentic", "saljpuls",
            "forefront-consulting".

    Returns:
        On success: {"status": "ok", "space_id": ..., "content": <feed text>}.
        On failure: {"status": "error", "error_message": ..., "available_spaces": [...]}.
    """
    available = sorted(p.stem for p in _FEED_DIR.glob("*.pdf"))
    pdf_path = _FEED_DIR / f"{space_id}.pdf"
    if not pdf_path.exists():
        return {
            "status": "error",
            "error_message": f"Unknown space_id {space_id!r}.",
            "available_spaces": available,
        }
    reader = pypdf.PdfReader(str(pdf_path))
    content = "\n".join(page.extract_text() or "" for page in reader.pages)
    return {"status": "ok", "space_id": space_id, "content": content}
