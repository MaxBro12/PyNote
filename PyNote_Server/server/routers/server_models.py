from pydantic import BaseModel


class UserModel(BaseModel):
    token: str
    username: str
    password: str


class CreateNoteModel(BaseModel):
    token: str
    username: str
    password: str
    note: str
    inner: str


class DeleteNoteModel(BaseModel):
    token: str
    username: str
    password: str
    note: str
