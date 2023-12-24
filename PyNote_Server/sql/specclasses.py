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


@dataclass
class UserNoteData:
    user: UserData
    notes: tuple[NoteData, ...]


class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance