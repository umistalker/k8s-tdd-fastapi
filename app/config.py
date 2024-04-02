import logging
import os
from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings

logger = logging.getLogger("uvicorn")


class EnumMixin:

    def format_value(self) -> str:
        value = self.value.replace('_', ' ')
        return value

    @classmethod
    def choices(cls) -> tuple:
        return tuple(
            (key.value, key.format_value()) for key in cls
        )


class EnvironmentType(EnumMixin, Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    STAGING = "staging"


class Settings(BaseSettings):
    environment: EnvironmentType = os.environ.get("ENVIRONMENT", EnvironmentType.choices())
    debug: bool = bool(os.environ.get('DUBUG', 0))
    database_url: str | None = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> Settings:
    logger.info("Loading config settings from the environment...")
    return Settings()
