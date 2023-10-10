from functools import lru_cache

from core import settings

environments = {
    settings.EnvironmentTypes.test: settings.TestSettings,
    settings.EnvironmentTypes.dev: settings.DevelopmentSettings,
    settings.EnvironmentTypes.prod: settings.ProductionSettings,
}


@lru_cache
def get_settings() -> settings.BaseAppSettings:
    app_env = settings.BaseAppSettings().environment
    return environments[app_env]()
