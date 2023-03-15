from dataclasses import dataclass

from domain.page import Page
from domain.post import Post


@dataclass
class Statistics:
    page: Page
    posts_on_page: list[Post] = None
