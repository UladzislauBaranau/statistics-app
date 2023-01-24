from src.core.exceptions import InvalidUserException
from src.domain.page import Page, PageStatistics
from src.domain.post import Post
from src.ports.repositories.pages_posts_repository import PagesPostsRepository


class InMemoryPagesPostsRepository(PagesPostsRepository):
    def __init__(self, page: Page) -> None:
        self.page = page

    async def get_posts_from_page(self, user_id: int) -> list[Post]:
        if self.page.page_owner.id == user_id:
            return self.page.posts

        raise InvalidUserException

    async def get_n_follow_requests_from_page(self, user_id) -> int:
        if self.page.page_owner.id == user_id:
            return self.page.n_follow_requests

        raise InvalidUserException

    async def get_info_about_pages(self, user_id) -> list:
        if self.page.page_owner.id == user_id:
            return [
                self.page.id,
                self.page.page_name,
                self.page.description,
                self.page.uuid,
                self.page.n_followers,
            ]

        raise InvalidUserException

    async def get_statistics_about_pages(self) -> PageStatistics:
        pass
