# from typing import TypedDict
from dataclasses import dataclass


@dataclass
class UserData:
    id: int
    username: str
    password: str


@dataclass
class NoteData:
    name: str
    inner: str
