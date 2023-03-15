from domain.page import Page
from domain.post import Post
from ports.repositories.pages_posts_repository import PagesPostsRepository


class InMemoryPagesPostsRepository(PagesPostsRepository):
    def __init__(self, page: object, post: object) -> None:
        self.page = page
        self.post = post

    async def get_info_about_pages(self, user_id: int) -> list[Page]:
        return [
            Page(
                id=self.page.id,
                page_name=self.page.page_name,
                description=self.page.description,
                uuid=self.page.uuid,
                n_followers=self.page.n_followers,
                n_follow_requests=self.page.n_follow_requests,
            )
        ]

    async def get_info_about_posts(self, user_id: int) -> list[Post]:
        return [Post(id=self.post.id, n_likes=self.post.n_likes, page_id=self.page.id)]
