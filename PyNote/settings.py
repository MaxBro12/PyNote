from typing import Final
from PySide6.QtCore import QSize, QMargins


# ! Основное
ERROR_FOUND: Final = 'Found error! Please link logger.log to developer\nError log:'
DIR_DATA: Final = 'data'
DIR_NOTES: Final = f'{DIR_DATA}/notes'
DIR_THEMES: Final = 'themes'

FILE_LOGGER: Final = 'logger.log'
FILE_LOGGER_MAX_LEN: Final = 1_000

FILE_SETTINGS: Final = f'{DIR_DATA}/settings.toml'
FILE_SETTINGS_IN: Final = {
    'MAIN': {
        'width': 1000,
        'height': 700,
        'opacity': 1.0,
        'lang': "ru",
        'theme': "dark.css",
        'font_editor_title_size': 15,
        'font_editor_text_size': 10,
        'font_notes_list_size': 12
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

# ! Настройки
SETTINGS_APP_SIZE: Final = (300, 400)
SETTINGS_APP_L_PANNEL_SIZE: Final = 150

# ! Приложение
NOTE_LIST_L_PANNEL_SIZE: Final = 200

EDITOR_TITLE_MAX_HEIGHT: Final = 30

SPACER_ITEM_SIZE: Final = (30, 5)

ALL_SPASING: Final = 2
ALL_MARGINS = QMargins(2, 2, 2, 2)

NOTE_LIST_ITEM = QSize(100, 45)
NOTE_LIST_ITEM_L = QSize(100, 40)
NOTE_LIST_ITEM_B = QSize(40, 40)
NOTE_LIST_ITEM_ICON = QSize(10, 10)

FILE_APP_ICON: Final = 'icons/icon.ico'
# file_settings_icon = 'PyNote/icons/settings.svg'
# file_delete_icon = 'PyNote/icons/delete.svg'
# file_sync_icon = 'PyNote/icons/sync.svg'
# file_new_note_icon = 'PyNote/icons/newnote.svg'

# ! Заметки
TITLE_MAX_LEN: Final = 16
NOTE_EXT: Final = '.md'
FILE_NOTE: Final = '_data.toml'
FILE_NOTE_SAMPLE: Final = {
    'sync': False,

    'last_save': '',

    'timer': False,
    'timer_at': '',
}

# ? Шрифты
FONT_NOTES_LIST_FAMILY: Final = 'Noto Sans Brahmi'
FONT_NOTES_LIST_SIZE: Final = 12
FONT_NOTES_LIST_BOND: Final = 0

FONT_EDITOR_TITLE_FAMILY: Final = 'Noto Sans Brahmi'
FONT_EDITOR_TITLE_SIZE: Final = 15
FONT_EDITOR_TITLE_BOND: Final = 0

FONT_EDITOR_TEXT_FAMILY: Final = 'Noto Sans'
FONT_EDITOR_TEXT_SIZE: Final = ''
FONT_EDITOR_TEXT_BOND: Final = 0


# ? Темы для приложения
FILE_TH_DARK: Final = 'data/themes/dark.toml'
FILE_TH_DARK_IN: Final = {
    'background': '#1e1e1e',
    'text_color': '#ffffff',
    'side_panel': '#252526',
    'file_settings_icon': 'icons/settings_light.svg',
    'file_delete_icon': 'icons/delete_light.svg',
    'file_sync_icon': 'icons/sync_light.svg',
    'file_new_note_icon': 'icons/newnote_light.svg',
    'file_expand_icon': "icons/expand_light.svg",
}
FILE_TH_LIGHT: Final = 'data/themes/light.toml'
FILE_TH_LIGHT_IN: Final = {
    'background': '#ffffff',
    'text_color': '#000000',
    'side_panel': '#f3f3f3',
    'file_settings_icon': 'icons/settings.svg',
    'file_delete_icon': 'icons/delete.svg',
    'file_sync_icon': 'icons/sync.svg',
    'file_new_note_icon': 'icons/newnote.svg',
    'file_expand_icon': "icons/expand.svg",
}
FILE_TH_SPACE: Final = 'data/themes/spacekit.toml'
FILE_TH_SPACE_IN: Final = {
    'background': '#2b303b',
    'text_color': '#ffffff',
    'side_panel': '#1c1f26',
    'file_settings_icon': 'icons/settings_light.svg',
    'file_delete_icon': 'icons/delete_light.svg',
    'file_sync_icon': 'icons/sync_light.svg',
    'file_new_note_icon': 'icons/newnote_light.svg',
    'file_expand_icon': "icons/expand_light.svg",
}

# ! Сервер
API_NEW: Final = "new"
API_USR: Final = "usr"
API_NOTE: Final = "note"
