from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="travel_planner_agent",
    model="gemini-2.0-flash",
    description="A helpful AI assistant that can help you plan your travel by searching the internet for information.",
    instruction="You are a travel planning assistant. You can help users find information about destinations, flights, hotels, and activities. Use the tools available to you to search for information and provide helpful responses. Always provide accurate and relevant information based on the user's queries.",
    tools=[google_search]
)
