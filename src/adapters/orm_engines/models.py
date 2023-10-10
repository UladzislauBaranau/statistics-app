from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()

association_table = Table(
    "pages_post_likes",
    Base.metadata,
    Column("users_user", ForeignKey("users_user.id")),
    Column("pages_post", ForeignKey("pages_post.id")),
)


class UsersORM(Base):
    __tablename__ = "users_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[list["PagesORM"]] = relationship()
    liked_posts: Mapped[list["PostORM"]] = relationship(secondary=association_table)


class PagesORM(Base):
    __tablename__ = "pages_page"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_owner_id: Mapped[int] = mapped_column(
        ForeignKey("users_user.id", ondelete="CASCADE"),
    )
    name: Mapped[str] = mapped_column(nullable=False)
    uuid: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    posts: Mapped[list["PostORM"]] = relationship()
    followers: Mapped[list["FollowersORM"]] = relationship()
    follow_requests: Mapped[list["FollowRequestsORM"]] = relationship()


class PostORM(Base):
    __tablename__ = "pages_post"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(
        ForeignKey("pages_page.id", ondelete="CASCADE"),
    )


class FollowersORM(Base):
    __tablename__ = "pages_page_followers"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(
        ForeignKey("pages_page.id", ondelete="CASCADE"),
    )


class FollowRequestsORM(Base):
    __tablename__ = "pages_page_follow_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(
        ForeignKey("pages_page.id", ondelete="CASCADE"),
    )
