from dataclasses import dataclass

from src.domain.post import Post
from src.domain.user import User


@dataclass
class Page:
    id: int
    page_name: str
    description: str
    uuid: str
    page_owner: User
    posts: list[Post]
    n_follow_requests: int
    n_followers: int


@dataclass
class PageStatistics:
    page: Page
