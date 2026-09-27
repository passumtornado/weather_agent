"""Application configuration"""

from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application Settings loaded from environment variables"""
    openai_api_key: SecretStr
    math_mcp_url: str = "http://localhost:8001/mcp"
    weather_mcp_url: str = "http://localhost:8000/mcp"
    model_name:str = "gpt-5-mini"
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    """Return cache application settings"""
    return Settings()