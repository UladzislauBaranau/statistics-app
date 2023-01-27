from sqlalchemy import select, func, distinct

from src.domain.post import Post
from src.core.exceptions import DatabaseConnectionException
from src.ports.repositories.pages_posts_repository import PagesPostsRepository

from src.adapters.orm_engines.models import (
    FollowersORM,
    PostORM,
    PostLikeORM,
    PagesORM,
    FollowRequestsORM,
)


class SQLAlchemyPagesPostsRepository(PagesPostsRepository):
    def __init__(self, db) -> None:
        self.db = db

    async def get_info_about_posts(self, user_id: int) -> list[Post]:
        try:
            query = (
                select(PostLikeORM.post_id, func.count(PostLikeORM.user_id))
                .join(PostORM, PostORM.id == PostLikeORM.post_id)
                .join(PagesORM, PagesORM.id == PostORM.page_id)
                .group_by(PostLikeORM.post_id)
                .where(PagesORM.page_owner_id == user_id)
            )

            posts_info = await self.db.execute(query)
            return [Post(id=info[0], n_likes=info[1]) for info in posts_info]

        except Exception:
            raise DatabaseConnectionException

    async def get_info_about_pages(self, user_id: int) -> list:
        try:
            query = (
                select(
                    PagesORM.id,
                    PagesORM.name,
                    PagesORM.description,
                    PagesORM.uuid,
                    func.count(distinct(FollowersORM.id)),
                    func.count(distinct(FollowRequestsORM.id)),
                )
                .join(FollowersORM, PagesORM.id == FollowersORM.page_id)
                .join(FollowRequestsORM, PagesORM.id == FollowRequestsORM.page_id)
                .where(PagesORM.page_owner_id == user_id)
                .group_by(PagesORM.id)
            )

            pages_info = await self.db.execute(query)
            return [info for info in pages_info]

        except Exception:
            raise DatabaseConnectionException
