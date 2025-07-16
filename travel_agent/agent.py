from google.adk.agents import Agent
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
import os
REMOTE_AGENT_URL = os.getenv('REMOTE_AGENT_URL', 'http://localhost:8001')

hotel_agent = RemoteA2aAgent(
    name="hotel_agent",
    description="A helpful AI assistant that can search and book hotels.",
    agent_card=(
        f"{REMOTE_AGENT_URL}/a2a/hotel_agent{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

plan_agent = RemoteA2aAgent(
    name="plan_agent",
    description="A helpful AI assistant that can plan your travel.",
    agent_card=(
        f"{REMOTE_AGENT_URL}/a2a/plan_agent{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    instruction="""
You are a helpful travel assistant that can help users plan their travel by searching for hotels and planning trips. You can search for hotels, book them, and cancel bookings. You can also help users plan their trips by searching the internet for information about destinations, flights, hotels, and activities.
You can use the tools available to you to search for information and provide helpful responses. Always provide accurate and relevant information based on the user's queries.
    """,
    global_instruction=(
        "You are a helpful travel assistant that can help users plan their travel by searching for hotels and planning trips. You can search for hotels, book them, and cancel bookings. You can also help users plan their trips by searching the internet for information about destinations, flights, hotels, and activities."
    ),
    sub_agents=[hotel_agent, plan_agent],
)
