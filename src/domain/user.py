from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    USER = "U"
    MODERATOR = "M"
    ADMIN = "A"


@dataclass
class User:
    id: int
    username: str
    role: Role
