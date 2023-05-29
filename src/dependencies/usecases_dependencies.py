from fastapi import Depends

from adapters.repositories.sqlalchemy_pages_posts_repository import (
    SQLAlchemyPagesPostsRepository,
)
from dependencies.authorization import get_token_payload
from dependencies.database import get_db
from use_cases.auth_management import AuthManagementUseCase
from use_cases.pages_statistics_management import PagesStatisticsManagementUseCase


def get_pages_statistics_management_use_case(db=Depends(get_db)):
    return PagesStatisticsManagementUseCase(SQLAlchemyPagesPostsRepository(db))


def get_current_user(payload_data=Depends(get_token_payload)):
    return AuthManagementUseCase(payload_data).get_current_user


def get_roles_admin_or_moderator(payload_data=Depends(get_token_payload)):
    return AuthManagementUseCase(payload_data).check_admin_or_moderator_roles
