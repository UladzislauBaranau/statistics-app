from fastapi.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

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
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Permission denied. Only for admin or moderator",
            )
