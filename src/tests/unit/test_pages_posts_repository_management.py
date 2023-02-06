import pytest

from src.adapters.repositories.memrepo import InMemoryPagesPostsRepository


@pytest.fixture
def memory_pages_posts_repository(page, post):
    return InMemoryPagesPostsRepository(page, post)


@pytest.mark.asyncio
async def test_get_info_about_pages(memory_pages_posts_repository, user):
    page = await memory_pages_posts_repository.get_info_about_pages(user_id=user.id)

    assert type(page) == list
    assert len(page) == 1
    assert type(page[0]) is not None


@pytest.mark.asyncio
async def test_get_info_about_posts(memory_pages_posts_repository, user):
    post = await memory_pages_posts_repository.get_info_about_posts(user_id=user.id)

    assert type(post) == list
    assert len(post) == 1
    assert type(post[0]) is not None
