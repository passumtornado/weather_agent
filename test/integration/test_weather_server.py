import pytest
from mcp import Client
from mcp_agent.servers.weather.server import mcp

@pytest.mark.asyncio
async def test_weather_server_expose_tools() -> None:
    async with Client(mcp) as client:
        result = await client.list_tools()
        tool_names = {
            tool.name
            for tool in result.tools
        }
        assert "get_forecast" in tool_names