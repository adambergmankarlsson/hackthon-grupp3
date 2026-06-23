"""Web search tool, exposed as a sub-agent.

The built-in `google_search` tool cannot be combined with custom function tools in
the same agent (Vertex: "Multiple tools are supported only when they are all search
tools"). So search lives in its own agent here, and the root agent calls it via an
AgentTool — which the model sees as just another callable function.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search


def build_search_agent(model: str) -> Agent:
    """Build the web-research sub-agent used by the root agent."""
    return Agent(
        name="search_agent",
        model=model,
        description="Searches the web for current news, trends and facts.",
        instruction=(
            "You are a web research assistant. Use the google_search tool to find "
            "current, factual information and return a concise, sourced summary."
        ),
        tools=[google_search],
    )
