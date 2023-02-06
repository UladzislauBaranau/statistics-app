from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()


class PostLikeORM(Base):
    __tablename__ = "pages_post_likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("pages_post.id"))
    users: Mapped["UsersORM"] = relationship(back_populates="posts")
    posts: Mapped["PostORM"] = relationship(back_populates="users")


class UsersORM(Base):
    __tablename__ = "users_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[list["PagesORM"]] = relationship()
    posts: Mapped[list["PostLikeORM"]] = relationship(back_populates="users")


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
    users: Mapped[list["PostLikeORM"]] = relationship(back_populates="posts")


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
