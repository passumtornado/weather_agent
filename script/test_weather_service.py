import asyncio
from mcp_agent.servers.weather.service import(WeatherService)

async def main()->None:
    service = WeatherService()
    # coordinates = await service.geocode(
    #     "Stockholm"
    # )
    weather = await service.get_forecast("Stockholm")
    print(weather.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())