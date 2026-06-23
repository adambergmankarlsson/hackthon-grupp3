# hackthon-grupp3

A starter [Google ADK](https://google.github.io/adk-docs/) (1.x) agent to build on.

## Setup

Uses **Vertex AI** via Google Cloud Application Default Credentials (no API key).

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Authenticate to GCP (forefront account + hackathon project):
   ```bash
   gcloud auth login adam.bergman-karlsson@forefront.se
   gcloud config set project hackathon2026-c-sbx-557a
   gcloud auth application-default login
   gcloud auth application-default set-quota-project hackathon2026-c-sbx-557a
   gcloud services enable aiplatform.googleapis.com
   ```
3. Config lives in [assistant/.env](assistant/.env) (already set for Vertex AI).

## Run

```bash
# Interactive terminal chat
uv run adk run assistant

# Or the local web UI (then open the printed URL)
uv run adk web
```

## Layout

```
assistant/
├── __init__.py        # exposes the package to ADK
├── agent.py           # root_agent + tools — start here
└── workvivo_feed/     # mockup of an internal Workvivo integration
    ├── catalog.md     # describes each space; injected into the agent's context
    └── *.pdf          # one exported feed per Workvivo space
```

Edit [assistant/agent.py](assistant/agent.py) to change the instructions, model,
or add tools (any plain Python function with type hints + a docstring).

### Tools

- **`fetch_workvivo_post(space_id)`** — mockup of the internal Workvivo feed. The
  agent reads [catalog.md](assistant/workvivo_feed/catalog.md) (injected into its
  instructions) to know which space to fetch, then this tool extracts that PDF's
  text. To swap in the real integration later, replace the PDF read with a
  Workvivo API call — the tool signature stays the same.
- **`search_agent` (AgentTool)** — live web research via the built-in
  `google_search`. It lives in its own sub-agent because Vertex forbids mixing
  `google_search` with custom function tools in one agent.
