from dataclasses import dataclass


@dataclass
class Post:
    id: int
    n_likes: int
    page_id: int
