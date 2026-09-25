import pytest
from mcp import Client

from mcp_agent.servers.math.server import mcp

@pytest.mark.asyncio
async def test_math_server_exposes_tools():
    async with Client(mcp) as client:
        result = await client.list_tools()
        tool_names = {
            tool.name
            for tool in result.tools
        }
        assert tool_names == {
            "add",
            "subtract",
            "multiply",
            "divide",
        }

@pytest.mark.asyncio
async def test_multiply_via_mcp()->None:
    async with Client(mcp) as client:
        result = await client.call_tool(
            "multiply",
            {
                "a":25,
                "b":10,
            }
        )
        assert result.structured_content =={
            "result":250
        }