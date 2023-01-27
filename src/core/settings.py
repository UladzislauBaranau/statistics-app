from enum import Enum
from typing import Any

from pydantic import BaseSettings, Field, SecretStr


class EnvironmentTypes(Enum):
    test: str = "test"
    local: str = "local"
    dev: str = "dev"
    prod: str = "prod"


class BaseAppSettings(BaseSettings):
    environment: EnvironmentTypes = Field(EnvironmentTypes.prod, env="API_ENVIRONMENT")
    debug: bool = True
    title: str = "Statistics service"
    version: str = "0.1.0"
    allowed_hosts: list[str] = ["*"]
    db_driver_name: str = "postgresql+asyncpg"
    db_host: str = Field("statictics-pg", env="DATABASE_HOST")
    db_username: str = Field("statictics", env="DATABASE_USERNAME")
    db_password: SecretStr = Field("statictics", env="DATABASE_PASSWORD")
    db_database: str = Field("statictics", env="DATABASE_NAME")
    db_port: int = 5432

    @property
    def get_db_creds(self) -> dict[str, Any]:
        return {
            "drivername": self.db_driver_name,
            "username": self.db_username,
            "host": self.db_host,
            "port": self.db_port,
            "database": self.db_database,
            "password": self.db_password.get_secret_value(),
        }

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
        }


class TestSettings(BaseAppSettings):
    environment: EnvironmentTypes = Field(EnvironmentTypes.test, env="API_ENVIRONMENT")
    title: str = "Test environment - Statistics service"


class LocalSettings(BaseAppSettings):
    title: str = "Local environment - Statistics service"


class DevelopmentSettings(BaseAppSettings):
    title: str = "Development environment - Statistics service"


class ProductionSettings(BaseAppSettings):
    title: str = "Production environment - Statistics service"
    debug: bool = False
