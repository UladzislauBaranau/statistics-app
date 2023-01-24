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


@pytest.fixture
def pages_posts_repository(session):
    return SQLAlchemyPagesPostsRepository(session)


@pytest.mark.asyncio
async def test_get_posts_from_page(pages_posts_repository, session):
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

    posts = await pages_posts_repository.get_posts_from_page(user_id=1)

    assert type(posts) == list
    assert len(posts) == 2


@pytest.mark.asyncio
async def test_get_n_follow_requests_from_pages(pages_posts_repository, session):
    follow_requests = await pages_posts_repository.get_n_follow_requests_from_page(
        user_id=1,
    )

    assert type(follow_requests) == list
    assert len(follow_requests) == 2


@pytest.mark.asyncio
async def test_get_info_about_pages(pages_posts_repository, session):
    pages_info = await pages_posts_repository.get_info_about_pages(user_id=1)

    assert type(pages_info) == list
    assert len(pages_info) == 2
