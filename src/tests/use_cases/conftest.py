import pytest

from src.domain.page import PageStatistics
from src.domain.user import User
from src.domain.post import Post


@pytest.fixture
def user():
    user = User(
        id=1,
        username="testuser",
    )
    return user


@pytest.fixture
def user_2():
    user_2 = User(
        id=2,
        username="testuser2",
    )
    return user_2


@pytest.fixture
def post():
    post = Post(
        id=1,
        n_likes=33,
    )
    return post


@pytest.fixture
def second_post():
    second_post = Post(
        id=2,
        n_likes=9,
    )
    return second_post


@pytest.fixture
def page(user, post, second_post):
    page = PageStatistics(
        id=1,
        page_name="testpage",
        description="testdescription",
        uuid="testuuid",
        page_owner=user,
        posts=[post, second_post],
        n_follow_requests=1,
        n_followers=2,
    )
    return page
