"""Forefront "Executive Research Agent" — Google ADK (1.x).

Combines internal Forefront knowledge (the Workvivo feed) with live web research to
generate newsletter material. Tools live in the `tools/` package; this module only
wires them onto the root agent.
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .tools import build_search_agent, fetch_workvivo_post, load_workvivo_catalog

MODEL = "gemini-2.5-flash"

search_agent = build_search_agent(MODEL)

root_agent = Agent(
    name="assistant",
    model=MODEL,
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
        '"Vilken åtgärd bör de överväga?".\n\n'
        "VERKTYG:\n"
        "- Använd `fetch_workvivo_post` för att hämta Forefronts interna "
        "Workvivo-flöde (vår expertis och våra affärshändelser). Välj rätt "
        "space_id utifrån katalogen nedan.\n"
        "- Använd `search_agent` för aktuella nyheter, trender och fakta från webben.\n\n"
        "=== WORKVIVO-KATALOG ===\n" + load_workvivo_catalog()
    ),
    tools=[fetch_workvivo_post, AgentTool(agent=search_agent)],
)
