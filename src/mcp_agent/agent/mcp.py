from mcp_agent.config import get_settings

def build_mcp_config() -> dict:
    settings = get_settings()

    return{
        "mcpServer":{
            "math":{
                "url":settings.math_mcp_url
            },
            "weather":{
                "url":settings.weather_mcp_url
            }
        }
    }