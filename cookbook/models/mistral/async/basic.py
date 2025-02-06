"""
Basic async example using Claude.
"""

import asyncio

from agno.agent.agent import Agent
from agno.models.mistral.mistral import MistralChat

agent = Agent(
    model=MistralChat(id="mistral-large-latest"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
