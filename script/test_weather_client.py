import asyncio
from mcp_agent.clients.mcp_client import MCPClient

WEATHER_SERVER_URL = (
    "http://localhost:8000/mcp"
)


async def main()->None:
   async with MCPClient(WEATHER_SERVER_URL) as client:
       tools = await client.list_tools()
       print("Available tools:")
       for tool in tools.tools:
           print(f"_{tool.name}")
       result = await client.call_tools(
           "get_forecast",
           {
               "location": "Paris"
           }
       )
       print("\nWeather data:")
       print(result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())