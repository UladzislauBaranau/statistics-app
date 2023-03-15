import pytest

from domain.page import Page
from domain.post import Post
from domain.user import User


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
        page_id=1,
    )
    return post


@pytest.fixture
def page():
    page = Page(
        id=1,
        page_name="testpage",
        description="testdescription",
        uuid="testuuid",
        n_follow_requests=1,
        n_followers=2,
    )
    return page
