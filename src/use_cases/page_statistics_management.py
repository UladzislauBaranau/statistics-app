from src.domain.page import PageStatistics
from src.domain.post import Post
from src.ports.repositories.pages_posts_repository import PagesPostsRepository


class PageStatisticsManagementUseCase:
    def __init__(self, pages_posts_repository: PagesPostsRepository) -> None:
        self.pages_posts_repository = pages_posts_repository

    async def get_posts(self, user_id: int) -> list[Post]:
        posts = await self.pages_posts_repository.get_posts_from_page(user_id)
        return posts

    async def get_n_follow_requests(self, user_id: int) -> int:
        follow_requests = (
            await self.pages_posts_repository.get_n_follow_requests_from_page(user_id)
        )
        return follow_requests

    async def get_pages_info(self, user_id: int) -> list:
        pages_info = await self.pages_posts_repository.get_info_about_pages(user_id)
        return pages_info

    async def get_statistics(self) -> PageStatistics:
        pages_statistics = await self.pages_posts_repository.get_statistics_about_pages()
        return pages_statistics
