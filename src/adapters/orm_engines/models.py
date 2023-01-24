from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UsersORM(Base):
    __tablename__ = "users_user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)


class PagesORM(Base):
    __tablename__ = "pages_page"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    uuid = Column(String, nullable=False)
    description = Column(String, nullable=False)
    page_owner_id = Column(Integer, ForeignKey("users_user.id", ondelete="CASCADE"))
    user = relationship("UsersORM", uselist=True)


class PostORM(Base):
    __tablename__ = "pages_post"

    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("pages_page.id", ondelete="CASCADE"))
    pages = relationship("PagesORM", uselist=True)


class PostLikeORM(Base):
    __tablename__ = "pages_post_likes"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("pages_post.id", ondelete="CASCADE"))
    posts = relationship("PostORM", uselist=True)
    user_id = Column(Integer, ForeignKey("users_user.id", ondelete="CASCADE"))
    users = relationship("UsersORM", uselist=True)


class FollowersORM(Base):
    __tablename__ = "pages_page_followers"

    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("pages_page.id", ondelete="CASCADE"))
    pages = relationship("PagesORM", uselist=True)


class FollowRequestsORM(Base):
    __tablename__ = "pages_page_follow_requests"

    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("pages_page.id", ondelete="CASCADE"))
    pages = relationship("PagesORM", uselist=True)
