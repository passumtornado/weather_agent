"""Weather MCP server"""
from mcp.server import MCPServer
from mcp_agent.servers.weather import tools
from mcp_agent.servers.weather.schemas import CurrentWeather

mcp = MCPServer(
    name="weather-server",
)

@mcp.tool()
async def get_forecast(location: str) -> CurrentWeather:
    """Get the current weather for given location or city"""
    return await tools.get_forcast(location)