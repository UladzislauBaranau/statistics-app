import pytest

from src.adapters.repositories.memrepo import InMemoryPagesPostsRepository


@pytest.fixture
def memory_pages_posts_repository(page):
    return InMemoryPagesPostsRepository(page)


@pytest.mark.asyncio
async def test_get_posts_from_page(memory_pages_posts_repository, user):
    posts = await memory_pages_posts_repository.get_posts_from_page(user.id)

    assert type(posts) == list
    assert len(posts) == 2


@pytest.mark.asyncio
async def test_get_follower_requests_from_page(memory_pages_posts_repository, user):
    follow_requests = (
        await memory_pages_posts_repository.get_n_follow_requests_from_page(user.id)
    )

    assert type(follow_requests) == int
    assert follow_requests == 1
