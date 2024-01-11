from dataclasses import dataclass


@dataclass
class UserData:
    id: int
    username: str
    password: str


@dataclass
class NoteData:
    id: int
    name: str
    inner: str
