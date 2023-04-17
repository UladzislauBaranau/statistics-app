import jwt
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from core.config import get_settings
from core.settings import BaseAppSettings


class AuthDependency(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(
        self, request: Request, settings: BaseAppSettings = Depends(get_settings)
    ) -> dict:
        try:
            auth_credentials: HTTPAuthorizationCredentials = await super().__call__(
                request
            )
            return self.decode_access_token(
                auth_credentials.credentials, settings.jwt_secret_key
            )

        except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Invalid token or expired token"
            )

    @staticmethod
    def decode_access_token(token: str, jwt_secret_key: str) -> dict:
        decoded_access_token = jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
        return decoded_access_token


get_token_payload = AuthDependency()


def get_user_id(payload: AuthDependency = Depends(get_token_payload)) -> int:
    return payload.get("id")


def get_user_role(payload: AuthDependency = Depends(get_token_payload)) -> str:
    return payload.get("role")
