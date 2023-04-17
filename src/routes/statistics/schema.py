from pydantic import BaseModel, Field


class Page(BaseModel):
    id: int = Field(ge=1)
    page_name: str = Field(max_length=80)
    description: str = Field(max_length=180)
    uuid: str = Field(max_length=30)
    n_followers: int = Field(ge=0)
    n_follow_requests: int = Field(ge=0)


class Post(BaseModel):
    id: int = Field(ge=1)
    n_likes: int = Field(ge=0)
    page_id: int = Field(ge=1)


class StatisticsResponse(BaseModel):
    page: Page
    posts_on_page: list[Post] | None
