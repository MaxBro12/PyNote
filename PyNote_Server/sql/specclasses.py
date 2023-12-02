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


class Singleton:
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
