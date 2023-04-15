from typing import TypedDict


# ! Основное
file_log = 'data/logger.log'
file_error = 'error.log'

fold_data = 'data'
file_conf = 'data/settings.toml'
file_conf_inner = {
    'app': {
        'width': 1000,
        'height': 700,
        'lang': "ru",
        'theme': "dark.toml",
        'opacity': 1,
    },
    'user': {
        'username': "",
        'password': "",
        'wtkey': "",
    },
    'server': {
        'host': "",
        'token': "",
    }
}
file_conf_row2 = r'\[app\]\nwidth = [\d]*\nheight = [\d]*\ntheme = "[\w]*' \
    r'\.toml"\nopacity = [^\n]*\n\n\[user\]\nusername = "[\w]*"\npasswor' \
    r'd = "[\w]*"\nwtkey = "[^"]*"\n\n\[ser' \
    r'ver\]\nhost = "[^"]*"\ntoken = "[\w]*"\n'
file_conf_row = r"""\[app\]
width = [\d]*
height = [\d]*
lang = "[\w]*"
theme = "[\w]*\.toml"
opacity = [^\n]*\n
\[user\]
username = "[\w]*"
password = "[\w]*"
wtkey = "[^"]*"\n
\[server\]
host = "[^"]*"
token = "[\w]*"
"""


# ! Заметки
title_max_length = 16
fold_notes = 'data/notes'
file_notes = '_data.toml'
file_notes_sample = {
    'sync': False,

    'last_save': '',

    'timer': False,
    'timer_at': '',
}

# ? Шрифты
font_notes_list_family = 'Noto Sans Brahmi'
font_notes_list_size = 12
font_notes_list_bond = 0

font_editor_title_family = 'Noto Sans Brahmi'
font_editor_title_size = 15
font_editor_title_bond = 0

font_editor_text_family = 'Noto Sans'
font_editor_text_size = ''
font_editor_text_bond = 0


# ! Приложение
file_icon = 'PyNote/icons/icon.ico'
file_settings_icon = 'PyNote/icons/settings.svg'
file_delete_icon = 'PyNote/icons/delete.ico'
file_sync_icon = 'PyNote/icons/sync.ico'
file_new_note_icon = 'PyNote/icons/newnote.ico'

# ? Темы для приложения
fold_themes = 'data/themes'
file_dark = 'data/themes/dark.toml'
file_dark_inner = {
    'background': '#1e1e1e',
    'text_color': '#ffffff',
    'side_pannel': '#252526',
}
file_light = 'data/themes/light.toml'
file_light_inner = {
    'background': '#ffffff',
    'text_color': '#000000',
    'side_pannel': '#f3f3f3',
}
file_space = 'data/themes/spacekit.toml'
file_space_inner = {
    'background': '#2b303b',
    'text_color': '#ffffff',
    'side_pannel': '#1c1f26',
}


# ! Сервер
api_1 = "http://192.168.1.64:3334"
api_new = "new"
api_usr = "usr"
api_notes = "note"

server_upload_note_after_changes = 5


# ! Доп классы
class Conf(TypedDict):
    app: dict
    user: dict
    server: dict


class Theme(TypedDict):
    background: str
    text_pannel: str
    side_pannel: str


class User_Data(TypedDict):
    id: int
    username: str
    password: str
    token: str


class UserNote(TypedDict):
    id: int
    username: str
    password: str
    token: str
    name: str
    inner: str


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
