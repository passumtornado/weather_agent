"""Weather domain tools"""
from mcp_agent.servers.weather.schemas import (CurrentWeather)
from mcp_agent.servers.weather.service import WeatherService

_service = WeatherService()

async def get_forcast(location: str) -> CurrentWeather:
    """Return current weather for given location"""
    return await _service.get_forecast(location)