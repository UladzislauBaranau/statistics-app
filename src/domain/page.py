from dataclasses import dataclass


@dataclass
class Page:
    id: int
    page_name: str
    description: str
    uuid: str
    n_followers: int
    n_follow_requests: int
