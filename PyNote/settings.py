
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
file_conf_row = r"""\[app\]
width = [\d]*
height = [\d]*
lang = "[\w]*"
theme = "[\w]*\.toml"
opacity = [^\n]*
font_editor_title_size = [\d]*
font_editor_text_size = [\d]*
font_notes_list_size = [\d]*\n
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
# file_settings_icon = 'PyNote/icons/settings.svg'
# file_delete_icon = 'PyNote/icons/delete.svg'
# file_sync_icon = 'PyNote/icons/sync.svg'
# file_new_note_icon = 'PyNote/icons/newnote.svg'

# ? Темы для приложения
fold_themes = 'data/themes'
file_dark = 'data/themes/dark.toml'
file_dark_inner = {
    'background': '#1e1e1e',
    'text_color': '#ffffff',
    'side_panel': '#252526',
    'file_settings_icon': 'PyNote/icons/settings_light.svg',
    'file_delete_icon': 'PyNote/icons/delete_light.svg',
    'file_sync_icon': 'PyNote/icons/sync_light.svg',
    'file_new_note_icon': 'PyNote/icons/newnote_light.svg',
    'file_expand_icon': "PyNote/icons/expand_light.svg",
}
file_light = 'data/themes/light.toml'
file_light_inner = {
    'background': '#ffffff',
    'text_color': '#000000',
    'side_panel': '#f3f3f3',
    'file_settings_icon': 'PyNote/icons/settings.svg',
    'file_delete_icon': 'PyNote/icons/delete.svg',
    'file_sync_icon': 'PyNote/icons/sync.svg',
    'file_new_note_icon': 'PyNote/icons/newnote.svg',
    'file_expand_icon': "PyNote/icons/expand.svg",
}
file_space = 'data/themes/spacekit.toml'
file_space_inner = {
    'background': '#2b303b',
    'text_color': '#ffffff',
    'side_panel': '#1c1f26',
    'file_settings_icon': 'PyNote/icons/settings_light.svg',
    'file_delete_icon': 'PyNote/icons/delete_light.svg',
    'file_sync_icon': 'PyNote/icons/sync_light.svg',
    'file_new_note_icon': 'PyNote/icons/newnote_light.svg',
    'file_expand_icon': "PyNote/icons/expand_light.svg",
}


# ! Сервер
api_new = "new"
api_usr = "usr"
api_notes = "note"
