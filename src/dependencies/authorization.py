from fastapi import Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette.requests import Request

from core.config import get_settings
from core.settings import BaseAppSettings
from use_cases.auth_management import decode_access_token


class AuthDependency(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(
        self, request: Request, settings: BaseAppSettings = Depends(get_settings)
    ) -> dict:
        auth_credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        return decode_access_token(
            auth_credentials.credentials, settings.jwt_secret_key
        )


get_token_payload = AuthDependency()
