
# ! Основное
file_log = 'data/logger.log'
file_error = 'error.log'

fold_data = 'data'
file_conf = 'data/settings.toml'
file_conf_inner = {
    'app': {
        'width': 1000,
        'height': 700,
        'theme': "dracula.toml",
    },
    'user': {
        'id': 0,
        'token': 0,
    }
}
file_conf_row = r'^\[app\]\nwidth = [\d]*\nheight = [\d]*\ntheme = "[\w]*' \
    r'\.toml"\n\n\[user\]\nid = [\d]*\ntoken = [\d]*\n'


# ! Все что касается заметок
fold_notes = 'data/notes'
file_notes = '_data.toml'
file_notes_sample = {
    'sync': False,

    'last_save': '',

    'timer': False,
    'timer_at': '',
}


file_icon = 'PyNote/icon.ico'
# ? Темы для приложения
fold_themes = 'data/themes'
file_dark = 'data/themes/dark.toml'
file_dark_inner = {
    'test': ''
}
file_light = 'data/themes/light.toml'
file_light_inner = {
    'test': ''
}


# ! Сервер
api_1 = "http://192.168.1.67:3334"
api_new = "/new/"
api_usr = "/usr/"
