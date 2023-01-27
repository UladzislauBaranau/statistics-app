from dataclasses import dataclass

from src.domain.post import Post
from src.domain.user import User


@dataclass
class PageStatistics:
    id: int
    page_name: str
    description: str
    uuid: str
    page_owner: User
    n_follow_requests: int
    n_followers: int
    posts: list[Post]
