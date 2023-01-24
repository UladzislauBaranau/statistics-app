from abc import ABC, abstractmethod

from src.domain.page import PageStatistics
from src.domain.post import Post


class PagesPostsRepository(ABC):
    @abstractmethod
    async def get_posts_from_page(self, user_id: int) -> list[Post]:
        pass

    @abstractmethod
    async def get_n_follow_requests_from_page(self, user_id: int) -> int:
        pass

    @abstractmethod
    async def get_info_about_pages(self, user_id) -> list:
        pass

    @abstractmethod
    async def get_statistics_about_pages(self) -> PageStatistics:
        pass
