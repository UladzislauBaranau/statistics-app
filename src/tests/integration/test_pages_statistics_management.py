import pytest
from src.adapters.repositories.sqlalchemy_pages_posts_repository import (
    SQLAlchemyPagesPostsRepository,
)

from src.adapters.orm_engines.models import (
    FollowersORM,
    UsersORM,
    PagesORM,
    PostORM,
    PostLikeORM,
    FollowRequestsORM,
)
from src.use_cases.pages_statistics_management import PagesStatisticsManagementUseCase


@pytest.fixture
def pages_posts_repository(session):
    return SQLAlchemyPagesPostsRepository(session)


@pytest.fixture
def pages_statistics_management_usecase(pages_posts_repository):
    return PagesStatisticsManagementUseCase(pages_posts_repository)


@pytest.mark.asyncio
async def test_pages_statistics(pages_statistics_management_usecase, session):
    session.add_all(
        [
            UsersORM(id=1, username="username"),
            UsersORM(id=2, username="username2"),
            PagesORM(
                id=1,
                name="testpage",
                page_owner_id=1,
                uuid="uuid",
                description="description",
            ),
            PagesORM(
                id=2,
                name="testpage2",
                page_owner_id=1,
                uuid="uuid2",
                description="description2",
            ),
            PostORM(id=1, page_id=1),
            PostORM(id=2, page_id=1),
            PostLikeORM(id=1, post_id=1, user_id=1),
            PostLikeORM(id=2, post_id=1, user_id=2),
            PostLikeORM(id=3, post_id=2, user_id=1),
            FollowersORM(id=1, page_id=1),
            FollowersORM(id=2, page_id=2),
            FollowRequestsORM(id=1, page_id=1),
            FollowRequestsORM(id=2, page_id=2),
        ]
    )
    session.commit()

    pages_statistics_user_id_1 = (
        await pages_statistics_management_usecase.get_statistics(user_id=1)
    )
    pages_statistics_user_id_2 = (
        await pages_statistics_management_usecase.get_statistics(user_id=2)
    )

    assert len(pages_statistics_user_id_1) == 2
    assert type(pages_statistics_user_id_1) == list

    assert len(pages_statistics_user_id_2) == 0
    assert type(pages_statistics_user_id_2) == list
