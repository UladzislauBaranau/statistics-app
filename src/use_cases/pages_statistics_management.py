from domain.statistics import Statistics
from ports.repositories.pages_posts_repository import PagesPostsRepository


class PagesStatisticsManagementUseCase:
    def __init__(self, pages_posts_repository: PagesPostsRepository) -> None:
        self.pages_posts_repository = pages_posts_repository

    async def get_statistics(self, user_id: int) -> list[Statistics]:
        l_pages_info = await self.pages_posts_repository.get_info_about_pages(
            user_id=user_id
        )
        l_posts_info = await self.pages_posts_repository.get_info_about_posts(
            user_id=user_id
        )

        return [
            Statistics(
                page=page_info,
                posts_on_page=[
                    post_info
                    for post_info in l_posts_info
                    if page_info.id == post_info.page_id
                ],
            )
            for page_info in l_pages_info
        ]
