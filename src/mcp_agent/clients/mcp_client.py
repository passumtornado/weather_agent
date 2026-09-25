# """Reusable MCP client wrapper"""
from types import TracebackType
from typing import Any,Self

from mcp import Client

class MCPClient:
    def __init__(self, server_url: str):
        self.server_url = server_url
        self._client = Client(server_url)
    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self
    async def __aexit__(self, exc_type:type[BaseException]|None, exc_value:BaseException|None, traceback:TracebackType) -> None:
        await self._client.__aexit__(exc_type, exc_value, traceback)

    async def list_tools(self)->Any:
        """Lists all the tools available"""
        return await self._client.list_tools()
    async def call_tools(self,name:str,arguments:dict[str,Any],)->Any:
        """Calls all the tools available"""
        return await self._client.call_tool(name,arguments)