from time import timezone
from typing import Any
import httpx
from mcp_agent.servers.weather.schemas import (Coordinates,CurrentWeather)

class WeatherService:
    """Client for retrieving weather data"""
    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
    def __init__(self,timeout:float = 10.0,)->None:
        self.timeout = timeout
    async def geocode(self,location:str) -> Coordinates:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(self.GEOCODING_URL,params={'name':location,'count':1,"language":"en","format":"json"})
            response.raise_for_status()
            data = response.json()
            results = data["results"]
            if not results:
                raise ValueError(
                    f"Location {location} returned no results"
                )
            result = results[0]
            return Coordinates(
                name=result['name'],
                latitude=result["latitude"],
                longitude=result["longitude"],
                country=result.get("country"),
                timezone=result.get("timezone"),
            )
    async def get_forecast(self,location:str) -> CurrentWeather:
        """Retrieves weather data for given location"""
        coordinates = await self.geocode(location)
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                self.FORECAST_URL,
                params={
                    "latitude":coordinates.latitude,
                    "longitude":coordinates.longitude,
                    "current":(
                        "temperature_2m,"
                        "apparent_temperature,"
                        "relative_humidity_2m,"
                        "weather_code,"
                        "wind_speed_10m,"
                    ),
                    "timezone":"auto"
                }
            )
            response.raise_for_status()
            data: dict[str, Any] = response.json()
        current = data.get("current")
        if not current:
            raise ValueError(
                f"Location {location} returned no results"
            )
        return CurrentWeather(
            location = coordinates.name,
            temperature_c=current["temperature_2m"],
            apparent_temperature_c=current["apparent_temperature"],
            relative_humidity_percent= current["relative_humidity_2m"],
            wind_speed=current["wind_speed_10m"],
            weather_code=current["weather_code"],
            observation_time=current["time"],
            timezone = data["timezone"]
        )