from mcp.server import MCPServer
from mcp_agent.servers.math import tools

mcp = MCPServer(
    name="math-server",
)

@mcp.tool()
def add(a:float, b:float) -> float:
    """Add two numbers"""
    return tools.add(a,b)

@mcp.tool()
def subtract(a:float, b:float) -> float:
    """Subtract two numbers"""
    return tools.subtract(a,b)

@mcp.tool()
def multiply(a:float, b:float) -> float:
    """Multiply two numbers"""
    return tools.multiply(a,b)

@mcp.tool()
def divide(a:float, b:float) -> float:
    """Divide two numbers"""
    return tools.divide(a,b)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        # host="127.0.0.1",
        port=8001,
    )