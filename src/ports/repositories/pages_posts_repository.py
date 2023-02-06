from abc import ABC, abstractmethod

from src.domain.page import Page
from src.domain.post import Post


class PagesPostsRepository(ABC):
    @abstractmethod
    async def get_info_about_posts(self, user_id: int) -> list[Post]:
        pass

    @abstractmethod
    async def get_info_about_pages(self, user_id: int) -> list[Page]:
        pass
