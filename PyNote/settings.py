
# ! Основное
file_log = 'data/logger.log'
file_error = 'error.log'

fold_data = 'data'
file_conf = 'data/settings.toml'
file_conf_inner = {
    'app': {
        'width': 500,
        'height': 500,
    },
    'user': {
        'id': 0,
        'token': 0,
    }
}
file_conf_row = r"^\[app\]\nwidth = [\d]*\nheight = [\d]*\n\n\[user]" \
    r"\nid = [\d]*\ntoken = [\d]*\n"

fold_notes = 'data/notes'
