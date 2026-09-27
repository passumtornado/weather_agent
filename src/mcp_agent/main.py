"""Command-line entry point for the MCP agent"""
import asyncio
from mcp_agent.agent.service import agent_service

async def main()->None:
    """Run the iterative agent"""
    async with agent_service() as agent:
        print()
        print("Math + Weather MCP Agent")
        print("........................")
        print("Type 'exit' to quit")
        print()

        while True:
            user_input = input("you: ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit"}:
                break
            try:
                result = await agent.ainvoke(
                    {
                        "messages":[
                            {
                                "role": "user",
                                "content": user_input,
                            }
                        ]
                    }
                )
                print("\n--- DEBUG TRACE ---")

                for message in result["messages"]:
                    print(f"\n{type(message).__name__}")

                    tool_calls = getattr(message, "tool_calls", None)

                    if tool_calls:
                        for tool_call in tool_calls:
                            print(f"Tool: {tool_call['name']}")
                            print(f"Arguments: {tool_call['args']}")

                    if message.content:
                        print(f"Content: {message.content}")

                print("\n--- END TRACE ---")
                final_message = result["messages"][-1]
                print()
                print("Agent:")
                print(final_message.content)
                print()
            except Exception as e:
                print()
                print(f"Agent error:{e}")
                print(final_message)
                print()
if __name__ == "__main__":
    asyncio.run(main())

