import jwt

from core.exceptions import AuthorizationException, PermissionDeniedException
from domain.user import Role


class AuthManagementUseCase:
    def __init__(self, token_payload: dict) -> None:
        self.token_payload = token_payload

    @property
    def get_current_user(self) -> int:
        return self.token_payload.get("id")

    @property
    def check_admin_or_moderator_roles(self) -> None:
        if self.token_payload.get("role") not in (
            Role.ADMIN.value,
            Role.MODERATOR.value,
        ):
            raise PermissionDeniedException


def decode_access_token(token: str, jwt_secret_key: str) -> dict:
    try:
        return jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError):
        raise AuthorizationException
