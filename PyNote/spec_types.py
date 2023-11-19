from typing import TypedDict, Literal


# ! Доп классы
class Config_app(TypedDict):
    width: int
    height: int
    lang: str
    theme: str
    opacity: float | int
    font_editor_title_size: int
    font_editor_text_size: int
    font_notes_list_size: int


class Config_user(TypedDict):
    username: str
    password: str
    wtkey: str


class Config_server(TypedDict):
    host: str
    token: str


class Config(TypedDict):
    app: Config_app
    user: Config_user
    server: Config_server


class Theme(TypedDict):
    background: str
    text_color: str
    side_panel: str
    file_settings_icon: str
    file_delete_icon: str
    file_sync_icon: str
    file_new_note_icon: str
    file_expand_icon: str


class User_Data(TypedDict):
    id: int
    username: str
    password: str
    token: str


class User_Note(TypedDict):
    id: int
    username: str
    password: str
    token: str
    name: str
    inner: str


class Server_Data(TypedDict):
    host: str
    token: str


class Server_Log(TypedDict):
    log: Literal[
        'user not found',
        'incorrect password',
        'note not found',
        'timeout'
    ]


# ==============================
class Load_User(TypedDict):
    username: str
    password: str


class Note(TypedDict):
    name: str
    inner: str


class Post_Note(TypedDict):
    id: int
    token: str
    name: str
    inner: str


class Get_User_Note(TypedDict):
    id: int
    token: str


class Delete_Note(TypedDict):
    id: int
    username: str
    password: str
    token: str
    name: str
