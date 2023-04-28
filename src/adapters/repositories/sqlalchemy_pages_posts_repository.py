from sqlalchemy import distinct, func, select
from sqlalchemy.exc import SQLAlchemyError

from adapters.orm_engines.models import (
    FollowersORM,
    FollowRequestsORM,
    PagesORM,
    PostORM,
)
from core.exceptions import DatabaseConnectionException
from domain.page import Page
from domain.post import Post
from ports.repositories.pages_posts_repository import PagesPostsRepository


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

            return [
                Page(
                    id=page[0],
                    page_name=page[1],
                    description=page[2],
                    uuid=page[3],
                    n_followers=page[4],
                    n_follow_requests=page[5],
                )
                for page in pages_info
            ]

        except SQLAlchemyError:
            raise DatabaseConnectionException

    async def get_info_about_posts(self, user_id: int) -> list[Post]:
        try:
            query = (
                select(PostORM.id, func.count(PostORM.id), PagesORM.id)
                .outerjoin(PagesORM, PostORM.page_id == PagesORM.id)
                .where(PagesORM.page_owner_id == user_id)
                .group_by(PostORM.id, PagesORM.id)
            )

            result = await self.db.execute(query)
            posts_info = result.all()

            return [
                Post(id=post[0], n_likes=post[1], page_id=post[2])
                for post in posts_info
            ]

        except SQLAlchemyError:
            raise DatabaseConnectionException
