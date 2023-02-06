from sqlalchemy import select, func, distinct

from src.domain.page import Page
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

    async def get_info_about_pages(self, user_id: int) -> list[Page]:
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
                .outerjoin(FollowersORM, PagesORM.id == FollowersORM.page_id)
                .outerjoin(FollowRequestsORM, PagesORM.id == FollowRequestsORM.page_id)
                .where(PagesORM.page_owner_id == user_id)
                .group_by(PagesORM.id)
            )

            result = await self.db.execute(query)
            pages_info = result.all()

            l_pages_info = []
            if pages_info:
                for page in pages_info:
                    l_pages_info.append(
                        Page(
                            id=page[0],
                            page_name=page[1],
                            description=page[2],
                            uuid=page[3],
                            n_followers=page[4],
                            n_follow_requests=page[5],
                        )
                    )

            return l_pages_info

        except Exception:
            raise DatabaseConnectionException

    async def get_info_about_posts(self, user_id: int) -> list[Post]:
        try:
            query = (
                select(PostORM.id, func.count(PostLikeORM.user_id), PagesORM.id)
                .outerjoin(PagesORM, PostORM.page_id == PagesORM.id)
                .outerjoin(PostLikeORM, PostORM.id == PostLikeORM.post_id)
                .where(PagesORM.page_owner_id == user_id)
                .group_by(PostORM.id, PagesORM.id)
            )

            result = await self.db.execute(query)
            posts_info = result.all()

            l_posts_info = []
            if posts_info:
                for post in posts_info:
                    l_posts_info.append(
                        Post(id=post[0], n_likes=post[1], page_id=post[2])
                    )

            return l_posts_info

        except Exception:
            raise DatabaseConnectionException
