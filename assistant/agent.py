"""A minimal Google ADK (1.x) agent — boilerplate to build on.

The only thing ADK requires from this module is a module-level `root_agent`.
This starter uses ADK's built-in `google_search` tool so the agent can ground
its answers with live web results.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="assistant",
    model="gemini-2.5-flash",
    description="A simple starter assistant that can search the web.",
    instruction=(
        "You are a friendly, concise assistant. "
        "Use the google_search tool to look things up when a question needs "
        "current or factual information, then answer based on the results."
    ),
    tools=[google_search],
)
