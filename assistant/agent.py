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
    description="Executive Research Agent for Forefront — generates newsletter material.",
    instruction=(
        'Du är en "Executive Research Agent" för Forefront. '
        "Din uppgift är att generera underlag för ett personligt nyhetsbrev genom "
        "att kombinera specifik kunddata med realtidsnyheter.\n\n"
        'Ditt mål är att hitta "The Sweet Spot" där följande tre områden möts:\n'
        "1. Kundens aktuella utmaningar och affärshändelser.\n"
        "2. Vår expertis och tjänsteutbud.\n"
        "3. Aktuella teknikskiften och marknadstrender.\n\n"
        "Analysera alltid informationen ur ett rådgivande perspektiv: "
        '"Vad innebär detta för läsaren idag?" och '
        '"Vilken åtgärd bör de överväga?".'
    ),
    tools=[google_search],
)
