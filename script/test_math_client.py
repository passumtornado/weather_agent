import asyncio
from mcp_agent.clients.mcp_client import MCPClient

MATH_SERVER_URL = "http://127.0.0.1:8000/mcp"

async def main()->None:
    # client = MCPClient(MATH_SERVER_URL)
    async with MCPClient(MATH_SERVER_URL) as client:
        tools = await client.list_tools()
        print("Available tools:")
        print(tools)

        result1 = await client.call_tools("multiply",{"a":10,"b":20})
        result2 = await client.call_tools("add", {"a": 200, "b": 17})

        print("\nResults:")
        print(result1, result2)


if __name__ == "__main__":
    asyncio.run(main())



