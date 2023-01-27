import pytest

from src.adapters.repositories.memrepo import InMemoryPagesPostsRepository


@pytest.fixture
def memory_pages_posts_repository(page):
    return InMemoryPagesPostsRepository(page)


@pytest.mark.asyncio
async def test_get_info_about_posts(memory_pages_posts_repository, user):
    posts = await memory_pages_posts_repository.get_info_about_posts(user_id=user.id)

    assert type(posts) == list
    assert len(posts) == 2


@pytest.mark.asyncio
async def test_get_info_about_pages(memory_pages_posts_repository, user):
    pages = await memory_pages_posts_repository.get_info_about_pages(user_id=user.id)

    assert type(pages) == list
    assert len(pages) == 6
