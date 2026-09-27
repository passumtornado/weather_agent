"""Lifecycle management for AI Agent"""
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

from mcp_agent.agent.prompt import SYSTEM_PROMPT
from mcp_agent.config import get_settings

@asynccontextmanager
async def agent_service()->AsyncIterator:
    """Create an agent connected to all configured MCP servers"""
    settings = get_settings()
    config = {
        "mcpServers": {
            "math": {
                "url": settings.math_mcp_url
            },
            "weather": {
                "url": settings.weather_mcp_url
            }
        }
    }
    async with MCPAdapter(config) as adapter:
        tools = await adapter.list_tools()
        agent = create_agent(model=f"openai:{settings.model_name}",tools=tools,system_prompt=SYSTEM_PROMPT)
        yield agent