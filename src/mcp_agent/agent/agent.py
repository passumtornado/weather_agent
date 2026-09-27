from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
# from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from mcp_agent import config
from mcp_agent.agent.prompt import SYSTEM_PROMPT
from mcp_agent.config import get_settings

from dotenv import load_dotenv
load_dotenv()

async def create_mcp_agent():
    settings = get_settings()

    config = {
        "mcpServers":{
            "math":{
            "url":settings.math_mcp_url
        },
        "weather":{
        "url":settings.weather_mcp_url
        }
        }
    }
    adapter = MCPAdapter(config)
    await adapter.__aenter__()
    tools = await adapter.list_tools()



    model = ChatOpenAI(
        model=settings.model_name,
        api_key=settings.ollama_api_key,
    )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent, adapter
