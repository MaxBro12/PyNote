from dataclasses import dataclass


# ! Доп классы
@dataclass
class User:
    token: str
    username: str
    password: str


@dataclass
class Note:
    name: str
    inner: str
