import os
from google.adk.agents import Agent
from google.adk.tools.toolbox_tool import ToolboxTool

TOOLBOX_URL = os.getenv('TOOLBOX_URL', 'http://localhost:5001')
toolbox = ToolboxTool(TOOLBOX_URL)

tools = toolbox.get_toolset(toolset_name='my-toolset')

prompt = """
  You're a helpful hotel assistant. You handle hotel searching, booking and
  cancellations. When the user searches for a hotel, mention it's name, id,
  location and price tier. Always mention hotel ids while performing any
  searches. This is very important for any operations. For any bookings or
  cancellations, please provide the appropriate confirmation. Be sure to
  update checkin or checkout dates if mentioned by the user.
  Don't ask for confirmations from the user.
"""

root_agent = Agent(
    model='gemini-2.0-flash',
    name='hotel_agent',
    description='A helpful AI assistant that can search and book hotels.',
    instruction=prompt,
    tools=tools
)
