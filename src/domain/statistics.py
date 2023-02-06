from dataclasses import dataclass

from src.domain.page import Page
from src.domain.post import Post


@dataclass
class Statistics:
    page: Page
    posts_on_page: list[Post] = None
