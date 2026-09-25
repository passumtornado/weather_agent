from pydantic import BaseModel, Field
class Coordinates(BaseModel):
    """Geographic Coordinates"""
    name:str
    latitude: float
    longitude: float
    country:str|None = None
    timezone:str|None = None

class CurrentWeather(BaseModel):
    """Normalized current weather information"""
    location:str
    temperature_c:float = Field(
        description="Temperature in Celcius"
    )
    apparent_temperature_c:float
    wind_speed:float
    weather_code:int
    observation_time:str
    relative_humidity_percent:float
    timezone:str