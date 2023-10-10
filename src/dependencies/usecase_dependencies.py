from fastapi import Depends

from adapters.repositories.sqlalchemy_pages_posts_repository import (
    SQLAlchemyPagesPostsRepository,
)
from dependencies.database import get_db
from use_cases.pages_statistics_management import PagesStatisticsManagementUseCase


def get_pages_statistics_management_use_case(db=Depends(get_db)):
    return PagesStatisticsManagementUseCase(SQLAlchemyPagesPostsRepository(db))
