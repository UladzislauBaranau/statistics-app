import pytest
from fastapi.exceptions import HTTPException

from use_cases.auth_management import AuthManagementUseCase


@pytest.fixture
def auth_admin_management(valid_admin_jwt_secret_key):
    return AuthManagementUseCase(valid_admin_jwt_secret_key)


@pytest.fixture
def auth_user_management(valid_user_jwt_secret_key):
    return AuthManagementUseCase(valid_user_jwt_secret_key)


def test_get_current_user(auth_admin_management):
    user_id = auth_admin_management.get_current_user

    assert type(user_id) == int
    assert user_id == 1


def test_check_admin_or_moderator_roles(auth_admin_management):
    assert auth_admin_management.check_admin_or_moderator_roles is None


def test_fail_check_admin_or_moderator_roles(auth_user_management):
    with pytest.raises(HTTPException):
        auth_user_management.check_admin_or_moderator_roles
