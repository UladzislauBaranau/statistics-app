from src.domain.page import PageStatistics
from src.ports.repositories.pages_posts_repository import PagesPostsRepository


class PageStatisticsManagementUseCase:
    def __init__(self, pages_posts_repository: PagesPostsRepository) -> None:
        self.pages_posts_repository = pages_posts_repository

    async def get_statistics(self, user_id: int) -> list[PageStatistics]:
        pages_info = self.pages_posts_repository.get_info_about_pages(user_id=user_id)
        posts_info = self.pages_posts_repository.get_info_about_posts(user_id=user_id)
        pass
